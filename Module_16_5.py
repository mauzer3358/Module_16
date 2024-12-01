from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List


app = FastAPI()
users = []

templates = Jinja2Templates(directory="templates")

class Users(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/user/{user_id}')
def get_user(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    else: raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def create_user(user: Users, username: str, age: int) -> str:
    if user.id is None:
        user.id = 1
    else:
        user.id = max((t.id for t in users), default=0) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f'{user}'

@app.put("/user/{user_id}/{username}/{age}")
def update_users(user_id: int, username: str, age = int) ->str:
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