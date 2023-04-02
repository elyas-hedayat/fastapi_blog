from datetime import datetime

from pydantic import BaseModel


class PostInSchema(BaseModel):
    title: str
    description: str


class PostOutSchema(PostInSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
