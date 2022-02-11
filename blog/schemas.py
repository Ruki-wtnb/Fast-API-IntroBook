from typing import Optional, List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    
    name: str
    email: str
    blogs: Optional[List[Blog]] = []

    class Config:
        orm_mode = True

class User(BaseModel):
    
    name: str
    email: str
    password: str

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser]

    class Config:
        orm_mode = True



