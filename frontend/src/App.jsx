import { useState, useEffect } from "react";
import DimensionsList from "./DimensionsList";
import "./App.css";
import DimensionsForm from "./DimensionsForm";

function App() {
  const [dimensions, setDimensions] = useState([]); //Manage by usestate, contacts is an array of contacs
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentDimensions, setcurrentDimensions] = useState({})
  const [dimensionsList, setDimensionsList] = useState([])
  console.log(dimensions)
  useEffect(() => {
    fetchDimensionsUsing()
    fetchDimensionsList()
  }, []);

  const fetchDimensionsUsing = async () => {
    const response = await fetch("http://127.0.0.1:8080/columns");
    const data = await response.json();
    setDimensions(data.dimensions);
  };

  //calling this api will run the dataframe builder and then give us the columns
  const fetchDimensionsList = async() => {
    const response = await fetch("http://127.0.0.1:8080/build_data_frame");
    const data = await response.json();
    console.log(data)
    setDimensionsList(data);
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setcurrentDimensions({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (dimensions) => {
    if (isModalOpen) return
    setcurrentDimensions(dimensions)
    setIsModalOpen(true)
  }

  //when we update, we close the modal window and fetch the contacts
  const onUpdate = () => {
    closeModal()
    fetchDimensionsUsing()
  }
  return (
    <>
      <DimensionsList dimensions={dimensions} updateDimensions={openEditModal} updateCallback={onUpdate} />
      <button onClick={openCreateModal}>Add another dimension</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <DimensionsForm existingList={currentDimensions} dimensionOptions={dimensionsList} updateCallback={onUpdate} />
        </div>
      </div>
      }
    </>
  );
}

export default App;