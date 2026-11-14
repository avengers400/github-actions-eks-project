
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deployed to AWS EKS using GitHub Actions"}

@app.get("/health")
def health():
    return {"status": "healthy"}
