from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import PostInSchema, PostOutSchema
from db import get_db
from models import Post

router = APIRouter(tags=['blog'])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[PostOutSchema], summary="get all blog object")
def get_all_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Post).offset(skip).limit(limit).all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=PostOutSchema, summary="get single blog object")
def get_single_post(id: int, db: Session = Depends(get_db)):
    blog = db.query(Post).filter(Post.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")
    return blog.first()


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=PostOutSchema,
             summary="create single object")
def create_post(data: PostInSchema, db: Session = Depends(get_db)):
    new_post = Post(title=data.title, description=data.description)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT, summary="delete post object")
def delete_post(id: int, db: Session = Depends(get_db)):
    post_object = db.query(Post).filter(Post.id == id).first()
    if post_object:
        post_object.delete()
        db.commit()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")


@router.put('/update/{id}', status_code=status.HTTP_200_OK, summary="update post object", response_model=PostOutSchema)
def update_blog(id: int, data: PostInSchema, db: Session = Depends(get_db)):
    post_object = db.query(Post).filter(Post.id == id)
    if post_object.first():
        post_object.update(dict(data))
        db.commit()
        return post_object.first()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")
