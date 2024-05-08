from config import db

class Dimensions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dimension_name = db.Column(db.String(80), unique=False, nullable=False)
    # last_name = db.Column(db.String(80), unique=False, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "dimension_name": self.dimension_name,
            # "lastName": self.last_name,
            # "email": self.email,
        }
    

