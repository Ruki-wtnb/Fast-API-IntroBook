from multiprocessing import synchronize
from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from ..schemas import Blog, ShowBlog

from .. import models
from ..database import engine, sessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash

from ..functions import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get('/', response_model=List[ShowBlog])
def all_fetch(db: Session=Depends(get_db)):
    return blog.get_all(db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id: int, response: Response, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    print(blog is None)
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')

    return blog

@router.post('/',  status_code=status.HTTP_201_CREATED)
def create(request: Blog, db:Session=Depends(get_db)):
    return blog.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')

    db.commit()

    return 'Update completed'


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f'Blog with the id {id} is not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return 'Deletion completed'