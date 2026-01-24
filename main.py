from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    # Use uvicorn.run instead of subprocess to keep the process alive
    uvicorn.run(app, host="0.0.0.0", port=8000)
