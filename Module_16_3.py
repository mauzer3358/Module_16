from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def all_messages() -> dict:
    return users

@app.post("/users/{username}/{age}")
async def create_message(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                       age: int = Path(ge = 18,le = 120, description="Enter age", example="24")) -> str:
    current_index = str(int(max(users, key=int))+1)
    message = "Имя: " + username + ", возраст: " + str(age)
    users[current_index] = message
    return f"User {current_index} is registered"

@app.put("/users/{user_id}/{username}/{age}")
async def update_message(user_id: Annotated[int, Path(ge = 1, le = 100, description="Enter User ID", example="1")],
                         username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                       age: int = Path(ge = 18,le = 120, description="Enter age", example="24")) -> str:
    message = "Имя: " + username + ", возраст: " + str(age)
    users[str(user_id)] = message
    return f"User {user_id} is updated"

@app.delete("/users/{user_id}")
async  def delete_message(user_id: Annotated[int, Path(ge = 1, le = 100, description="Enter User ID", example="1")]) -> str:
    print(users)
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'

