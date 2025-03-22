from fastapi import FastAPI
import uvicorn
import subprocess
import os


app = FastAPI()

@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    subprocess.Popen(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])
