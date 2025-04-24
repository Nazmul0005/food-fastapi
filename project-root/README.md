# Contents of `README.md`

# Project Title

A brief description of the project and its purpose.

## Overview

This project is a web application that utilizes FastAPI for the backend and Streamlit for the frontend. The backend handles image analysis using AI models, while the frontend provides an interface for users to upload images and view analysis results.

## Directory Structure

- **backend/**: Contains the FastAPI application.
  - **src/**: Source code for the backend.
    - **main.py**: Entry point for the FastAPI application.
    - **router.py**: Defines API routes.
    - **models/**: Contains Pydantic models for data validation.
    - **services/**: Contains business logic for image analysis.
  - **requirements.txt**: Lists backend dependencies.
  - **README.md**: Documentation for the backend.

- **frontend/**: Contains the Streamlit application.
  - **src/**: Source code for the frontend.
    - **streamlit.py**: Streamlit application code.
  - **requirements.txt**: Lists frontend dependencies.
  - **README.md**: Documentation for the frontend.

## Installation

1. Clone the repository.
2. Navigate to the `backend` directory and install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Navigate to the `frontend` directory and install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the backend server:
   ```
   uvicorn src.main:app --reload
   ```
2. Run the Streamlit application:
   ```
   streamlit run src/streamlit.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.