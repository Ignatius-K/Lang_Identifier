# Python Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Local Libraries
from app.routers.detect import router as detect_router

# from database import models
# from database.db import engine, local_session
# from sqlalchemy.orm import Session

app = FastAPI(
    title="Language Identifier",
    description="""
        Aims to identify the language of specified text
    """
)

# Define origins
origins = ["*"]

# Include middleware
app.add_middleware(
    CORSMiddleware,
    # allow_credentials=False,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=origins
)


# Include routes
@app.get("/")
def welcome():
    return {
        "message": "Hello world"
    }


app.include_router(
    router=detect_router,
    prefix="/detect"
)
