from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from cruds import post_crud as crud
from schemas import post_schema

from dependencies import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.post("/{user_id}/", status_code=status.HTTP_201_CREATED, response_model=post_schema.Post)
async def create_post(user_id: int, post: post_schema.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post, user_id=user_id)


@router.get("/", response_model=List[post_schema.Post])
async def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts


@router.put("/{post_id}/", response_model=post_schema.Post)
async def update_post(post_id: int, post: post_schema.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db, post_id, post)
    return db_post