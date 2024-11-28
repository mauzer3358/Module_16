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
        user.id = max((t.id for t in users), default=0) + 1 #max(id_list, default=0) + 1
    user.username = username
    user.age = age
    users.append(user)
    # for t in user:
    #     print(t)
    return f"User {user} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_users(user_id: int, username: str, age = int) ->str:
    if user_id in [t.id for t in users]:
        count = 0
        for i in users:
            if users[count].id == user_id:
                users[count].username = username
                users[count].age = age
                return f'User ID = {users[count]} updated'
            else: count+=1
    else: raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_message(user_id: int) -> str:
    if user_id in [t.id for t in users]:
        count = 0
        for i in users:
            if i.id == user_id:
                deleted_user = users[count]
                break
            else:
                count+=1
        #print('True')
        users.pop(count)
        return f"User {deleted_user} deleted!"
    else: raise HTTPException(status_code=404, detail="User was not found")