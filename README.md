
# FastAPI Hello World Application

This is a simple FastAPI application that provides a "Hello, World!" message when accessed.

## Features

- **Hello Endpoint:** Returns a simple JSON response with a greeting message.
- **Swagger UI:** Auto-generated interactive API documentation.
- **ReDoc:** Alternative API documentation format.

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-name>

2. Install the required dependencies:

pip install fastapi uvicorn



Running the Application

1. Save the main application code in a file named main.py:

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}


2. Run the application using uvicorn:

uvicorn main:app --reload


3. Access the application:

Hello Endpoint: http://127.0.0.1:8000/hello

Swagger Documentation: http://127.0.0.1:8000/docs

ReDoc Documentation: http://127.0.0.1:8000/redoc




Requirements

Python 3.7+

FastAPI

Uvicorn


Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

License

This project is licensed under the MIT License.
