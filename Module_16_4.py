from fastapi import FastAPI, status, Body, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class Users(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
def get_all_users() -> List[Users]:
    return users

@app.post("/user/{username}/{age}")
def create_user(user: Users, username: str, age: int) -> str:
    if user.id is None:
        user.id = 1
    else:
        user.id = max((t.id for t in users), default=0) + 1
    user.username = username
    user.age = age
    users.append(user)
    print(user)
    return f'{user}'



@app.put("/user/{user_id}/{username}/{age}")
def update_users(user_id: int, username: str, age: int) ->str:
    for user in users:
        if user.id == user_id:
            user.id = user_id
            user.username = username
            user.age = age
            return user
        else: raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_message(user_id: int) -> str:
    for user in users:
        if user.id == user_id:
            users.pop(user)
            return user
    else: raise HTTPException(status_code=404, detail="User was not found")