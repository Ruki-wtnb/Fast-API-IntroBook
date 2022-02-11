from multiprocessing import synchronize
from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from ..schemas import User, ShowUser

from .. import models
from ..database import engine, sessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash


router = APIRouter(
    prefix="/user",
    tags=['users']
    )

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def all_fetch_users(db: Session=Depends(get_db)):
    users = db.query(models.User).all()

    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no users in this system')
    
    return users

    
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session=Depends(get_db)):

    hashed_password = Hash.bcrypt(request.password)
    
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user