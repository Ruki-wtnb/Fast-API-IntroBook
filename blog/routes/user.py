from multiprocessing import synchronize
from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from ..schemas import User, ShowUser

from .. import models
from ..database import engine, sessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash
from ..functions import user

router = APIRouter(
    prefix="/user",
    tags=['users']
    )

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def all_fetch_users(id: int, db: Session=Depends(get_db)):
    return user.show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session=Depends(get_db)):
    return user.create(request, db)