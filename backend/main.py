from flask import request, jsonify
from config import app, db
from models import Dimensions
from Dataframe_builder import startBuilder
from Scraper_v2 import scraper_run, data_crawling
import requests
import csv
from flask_cors import CORS





CORS(app) 

@app.route("/clusters",methods = ["GET"])
def getClusters():
    url = "http://127.0.0.1:8080/columns"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        columns_data = response.json()  # Parse response JSON
        print("Columns data:", columns_data)
    except requests.exceptions.RequestException as e:
        print("Error:", e)



    # Extract values excluding numeric values
    values_list = []
    for item in columns_data['dimensions']:
        values_list.append(item['dimension_name'])

    return scraper_run(values_list, 50)




@app.route("/columns", methods=["GET"])
def get_columns():
    columns = Dimensions.query.all()
    json_columns = list(map(lambda x: x.to_json(), columns))
    return jsonify({"dimensions": json_columns})

@app.route("/build_data_frame", methods=["GET"])
def buildDataFrame():
    startBuilder()
    with open('full_dataframe.csv') as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)
    print(columns)
    # json_columns = list(map(lambda x: x.to_json(), columns))
    return columns

@app.route("/create_dimension", methods=["POST"])
def create_dimension():
    dimension = request.json.get("dimension_name")
    print(dimension)
    if not dimension:
        return (
            jsonify({"message": "You must include a dimension"}),
            400,
        )
    newDimension = Dimensions(dimension_name=dimension)
    try:
        db.session.add(newDimension)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 200

@app.route("/update_dimension/<int:dimension_id>", methods=["PATCH"])
def update_contact(dimension_id):
    toBeUpdated = Dimensions.query.get(dimension_id)
    print(toBeUpdated)
    if not toBeUpdated:
        return jsonify({"message": "Dimension not found"}), 404
    data = request.json
    print(data)
    toBeUpdated.dimension_name = data.get("dimension_name", toBeUpdated.dimension_name)
    db.session.commit()
    return jsonify({"message": "Dimensions updated."}), 200

@app.route("/delete_dimension/<int:user_id>", methods=["DELETE"])
def delete_dimension(user_id):
    toBeDeleted = Dimensions.query.get(user_id)
    if not toBeDeleted:
        return jsonify({"message": "Dimension not found"}), 404
    db.session.delete(toBeDeleted)
    db.session.commit()
    return jsonify({"message": "Dimension deleted!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)