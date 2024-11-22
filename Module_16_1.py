from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcom() -> dict:
    return {"message": f"Главная страница"}

@app.get("/user/admin")
async def news() -> dict:
    return {"message": f'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user_id(user_id: str) -> dict:
        return {"User": f'Вы вошли как пользователь №, {user_id}'}

@app.get("/user")
async def id_paginator(username: str= "Mike" , age: int = 50) -> dict:
    return {"User": username, "Age": age}


