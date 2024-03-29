from typing import List
from pydantic import BaseModel

from schemas.post_schema import Post


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    posts: List[Post] = []