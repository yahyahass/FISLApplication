# FISL Application
### Overview
The `cx4242_proj` is a versatile web application developed using a React frontend and a Python Flask backend. This project utilizes a robust set of libraries and dependencies to deliver powerful data processing and visualization capabilities, particularly focused on clustering and modeling risk in various domains.

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
   conda activate cx4242_proj
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

### Usage
This tool is designed for users needing to perform risk analysis using clustering techniques. Users can input their data, select parameters for clustering, and visualize the results interactively through the web interface.

### Support
For any issues or contributions, please refer to the project's GitHub issues page or submit a pull request.

This README provides a concise introduction to setting up and getting started with the `cx4242_proj`. It lays the foundation for developers to engage with the project effectively.
