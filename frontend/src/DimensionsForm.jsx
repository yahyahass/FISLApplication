import { useState } from "react";

const DimensionsForm = ({ existingList = {}, dimensionOptions = [], updateCallback }) => {
    const [dimension_name, setDimensionName] = useState(existingList.dimension_name || "");
    const updating = Object.entries(existingList).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()
        const data = {
            dimension_name
        }
        console.log(data)
        const url = "http://127.0.0.1:8080/" + (updating ? `update_dimension/${existingList.id}` : "create_dimension")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        console.log(url, options)
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="dimension_name">Dimension:</label>
                <select
                    id="dimension_name"
                    value={dimension_name}
                    onChange={(e) => setDimensionName(e.target.value)}
                >
                    {dimensionOptions.map(option =>(
                        <option key = {option} value = {option}>{option}</option>
                    ))}
                </select>

            </div>            
            <button type="submit">{updating ? "Update" : "Add"}</button>
        </form>
    );
};

export default DimensionsForm