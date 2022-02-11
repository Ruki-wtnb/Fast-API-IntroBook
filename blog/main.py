# uvicorn blog.main:app --reload --host 0.0.0.0 --port 8000

from multiprocessing import synchronize
from fastapi import FastAPI
from .models import Base
from .database import engine, get_db, sessionLocal
from typing import List
from .routes import blog, user

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(engine)