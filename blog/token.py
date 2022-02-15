from hashlib import algorithms_available
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

from blog.schemas import TokenData

from sqlalchemy.orm import Session
from .functions.user import show
from database import get_db

SECRET_KET = "290e1681782b87dde6dceb07737c926bccdbb7266c0d2a93e77d50393e0d6caf"
ALGORITHEM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KET, algorithm=ALGORITHEM)

    return encoded_jwt

def verify_token(token: str, db: Session, credential_exception):
    try:
        payload = jwt.decoded(token, SECRET_KET, algorithms=[ALGORITHEM])
        email: str= payload.get("sub")
        id: int = payload.get("id")
        if email is None:
            raise credential_exception
        token_data = TokenData(email=email)

    except jwt.JWTError:
        raise credential_exception

    user = show(id, db)
    return user


