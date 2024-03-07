from models import post_model as models
from sqlalchemy.orm import Session
from schemas import post_schema


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: post_schema.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post_id: int, post: post_schema.PostCreate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post