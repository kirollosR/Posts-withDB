# from typing import Annotated

from fastapi import FastAPI
from database import engine, SessionLocal
from routers import users

import models

app = FastAPI()

app.include_router(users.router)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome To Our Blog API"}

