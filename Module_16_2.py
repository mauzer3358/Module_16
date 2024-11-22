from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcom() -> dict:
    return {"message": f"Главная страница"}

@app.get("/user/admin")
async def news() -> dict:
    return {"message": f'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user_id(user_id: int = Path(ge = 1, le = 100, description="Enter User ID", example="1")) -> dict:
        return {"User": f'Вы вошли как пользователь №, {user_id}'}

@app.get("/user/{username}/{age}")
async def id_paginator(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                       age: int = Path(ge = 18,le = 120, description="Enter age", example="24") ) -> dict:
    return {"User": username, "Age": age}