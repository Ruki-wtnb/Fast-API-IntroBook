from fastapi import APIRouter, Depends, HTTPException, status
from .. import models
from ..schemas import Login
from ..hashing import Hash
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Auth']
)

@router.post('/login')
def login(request: Login, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
    
    return user
