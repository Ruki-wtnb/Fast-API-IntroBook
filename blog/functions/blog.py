from .. import models
from ..schemas import Blog
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(blog: Blog, db:Session, current_user):
    user_id = [d for d in current_user]
    user_id = user_id[0].id

    new_blog = models.Blog(title=blog.title, 
    body=blog.body, user_id=user_id)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog