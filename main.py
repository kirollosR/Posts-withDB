# from typing import Annotated

from fastapi import FastAPI
from database import engine, SessionLocal
from routers import users

from models import user_model, post_model

app = FastAPI()

app.include_router(users.router)

# Create the database tables
models = [user_model, post_model]
for model in models:
    model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Welcome To Our Blog API"}

