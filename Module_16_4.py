from fastapi import FastAPI, status, Body, HTTPException
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
        user.id = len(users)+1
    user.username = username
    user.age = age

    users.append(user)
    return f"User {username} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_users(user_id: int, username: str, age = int) ->str:
    try:
        edit_user = users[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return f'User {user_id} updated'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_message(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f"Message ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")