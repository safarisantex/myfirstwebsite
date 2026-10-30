from fastapi import FastAPI
import models
from database import engine
from auth import router as auth_router

# Build database tables automatically on launch
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Render Deployment Website")

# Mount the auth backend router modules
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "Welcome to your Render-hosted FastAPI website!",
        "docs_url": "/docs"
    }
