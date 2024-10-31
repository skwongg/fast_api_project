from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HelloResponse(BaseModel):
    message: str
    
class HomeResponse(BaseModel):
    message: str

@app.get("/hello", response_model=HelloResponse)
async def hello():
    return {"message": "Hello from FastAPI in Docker and Kubernetes!"}

@app.get("/", response_model=HomeResponse)
async def home():
    return {"message": "Welcome home"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
