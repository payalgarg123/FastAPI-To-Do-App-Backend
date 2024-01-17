# FastAPI-To-Do-App-Backend
**Description**

This repository contains the backend code for a To-Do application built with FastAPI. The API allows users to manage their tasks by providing endpoints for creating, updating, deleting, and retrieving tasks.

**Features**

Task creation, modification, and deletion
Task retrieval based on various filters
User authentication for personalized task management

**Technologies Used**

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for Python.
Pydantic: Data validation and settings management using Python type annotations.
uvicorn: ASGI server for FastAPI.

**Installation**

git clone https://github.com/your-username/fastapi-todo-backend.git
cd fastapi-todo-backend
pip install -r requirements.txt
Configure the database settings in config.py:
DATABASE_URL = "sqlite:///./test.db"  # Use your preferred database URL
Run the application:
uvicorn main:app --reload
API Documentation
Access the Swagger documentation at http://localhost:8000/docs for detailed information about available API endpoints and how to use them.

**Usage**

Authentication
To access personalized task management, users need to authenticate. Use the /token endpoint with your credentials to obtain a token for subsequent requests.

Contributing
If you'd like to contribute to this project, please follow the Contribution Guidelines.

License
This project is licensed under the MIT License
