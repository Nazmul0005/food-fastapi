# Backend FastAPI Application

This is the backend part of the project, built using FastAPI. It provides an API for analyzing food images and returning relevant information.

## Project Structure

- `src/main.py`: Entry point of the FastAPI application.
- `src/router.py`: Defines the API routes.
- `src/models/schemas.py`: Contains Pydantic models for data validation.
- `src/services/analysis.py`: Implements the business logic for image analysis.
- `requirements.txt`: Lists the dependencies required for the backend.

## Getting Started

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`.