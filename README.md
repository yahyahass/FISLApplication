# FSIL Application LLM Inference:
Please find the pdf of project report (please note this was finished on an old ubuntu library computer and my ipad due to my laptop breaking down, sorry for the inconvenience and thanks!)

Link to google colab implementation: https://colab.research.google.com/drive/1XWBSsQwNtV5aNEOVTXQNJDP2_ZesD6WY?usp=sharing


# FSIL Application Visualization set up guide
### Overview
The `FSILApplication` is a versatile web application developed using a React frontend and a Python Flask backend. This project utilizes a robust set of libraries and dependencies to deliver powerful data processing and visualization capabilities, particularly focused on clustering and modeling risk in various domains.

### Environment Setup
This project relies on a Conda environment for managing its dependencies to ensure compatibility and ease of setup. The environment includes essential libraries such as Flask for the backend API, Beautifulsoup4 for web scraping, NumPy and Pandas for data handling, and Matplotlib and Scikit-learn for data visualization and machine learning.

### Key Dependencies
- **Python 3.12.2**: Core programming language
- **Flask**: Web framework for building the backend
- **React**: JavaScript library for building the user interface
- **Beautifulsoup4**: Library for parsing HTML and XML documents
- **Pandas and NumPy**: For advanced data manipulation and numerical analysis
- **Scikit-learn**: Machine learning library for modeling and clustering analysis
- **Matplotlib**: Plotting library for creating static, interactive, and animated visualizations

### Installation
To install and activate this environment:
1. Ensure you have Conda installed on your machine.
2. Clone the repository and navigate to the project directory.
3. Run the following commands:
   ```bash
   conda env create -f environment.yml
   conda activate FSILApplication
   ```

### Running the Application
to install all necessary packages.

Using two terminals,
Terminal 1 :
```bash
./backend/ folder, run $python main.py
```
Terminal 2 :
```bash
In ./frontend/ folder, run $yarn install

In ./frontend/ folder, run $npm run dev
```

direct local host link appears in terminal

