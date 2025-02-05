How to Create a Virtual Environment for Python:
1. Open the Command Prompt
2. Navigate to the directory where you want to create the virtual environment
3. Type the following command:
    `python -m venv venv`
    where `venv` is the name of your virtual environment
4. Activate the virtual environment
    `source myenv\Scripts\activate`
5. Install the required packages
    `pip install fastapi uvicorn`
6. Deactivate the virtual environment
    `deactivate`
7. Run the FastAPI application
    `uvicorn main:app --reload`
8. Open a browser and navigate to `http://localhost:8000` to test the application