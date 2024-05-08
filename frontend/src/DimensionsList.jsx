import React from "react"

const DimensionsList = ({ dimensions, updateDimensions, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:8080/delete_dimension/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Dimensions</h2>
        <table>
            <thead>
                <tr>
                    <th>Dimension</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {dimensions.map((dimension) => (
                    <tr key={dimension.id}>
                        <td>{dimension.dimension_name}</td>
                        <td>
                            <button onClick={() => updateDimensions(dimension)}>Update</button>
                            <button onClick={() => onDelete(dimension.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default DimensionsList