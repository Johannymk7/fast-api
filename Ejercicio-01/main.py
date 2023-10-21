from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = {
     0: {"name": "john1", "email": "email@example.com", "age": 20},
}

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


@app.get("/")
def home():
    return {"mensaje": "Hello World"}


@app.post("/users")
def create_user(user: User):
    database[user.id] = user
    return {"message": "Usuario creado correctamente"}


@app.get("/user")
def get_all_user():
    return list(database.values())


@app.get("/users")
def get_user(user_id: int):
    user = database.get(user_id)
    if user:
        return user
    return {"error": "Usuario no encotrdo"}


@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in database:
        database[user_id] = user
        return {"mensaje": "Usuario actualizado correctamente"}
    return {"error": "Usuario no encontrado"}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id in database:
        del database[user_id]
        return {"mensaje": "Usuario borrado correctamente"}
    return {"error": "Usuario no encontrado"}



