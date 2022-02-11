from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user/")
def create_user(user: User):
    return {"res": "ok", "ID": user.user_id, "名前": user.name}