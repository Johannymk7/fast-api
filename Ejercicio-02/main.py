from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = {
     0: {"id": 0 , "name": "john  ", "email": "john@example.com  ", "age": 20},
     1: {"id": 1 , "name": "john1 ", "email": "john1@example.com ", "age": 22},
     2: {"id": 2 , "name": "Alex  ", "email": "alex@example.com  ", "age": 28},
     3: {"id": 3 , "name": "javier", "email": "javier@example.com", "age": 30},
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
def get_all_users(name: str = None, email: str = None, age: int = None):
        # Lista para almacenar los usuarios filtrados
        filtered_users = []

        # Iterar sobre todos los usuarios en la base de datos
        for user in database.values():
            # Verificar si se proporcionan tanto el nombre, el correo electrónico y la edad
            if name and email and age:
                # Si el nombre, el correo electrónico y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
                if user.name == name and user.email == email and user.age == age:
                    filtered_users.append(user)
            # Verificar si se proporciona solo el nombre y la edad
            elif name and age:
                # Si el nombre y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
                if user.name == name and user.age == age:
                    filtered_users.append(user)
            # Verificar si se proporciona solo el correo electrónico y la edad
            elif email and age:
                # Si el correo electrónico y la edad coinciden con los proporcionados, se agrega el usuario a la lista filtrada
                if user.email == email and user.age == age:
                    filtered_users.append(user)
            # Verificar si se proporciona solo el nombre
            elif name:
                # Si el nombre coincide con el proporcionado, se agrega el usuario a la lista filtrada
                if user.name == name:
                    filtered_users.append(user)
            # Verificar si se proporciona solo el correo electrónico
            elif email:
                # Si el correo electrónico coincide con el proporcionado, se agrega el usuario a la lista filtrada
                if user.email == email:
                    filtered_users.append(user)
            # Verificar si se proporciona solo la edad
            elif age:
                # Si la edad coincide con la proporcionada, se agrega el usuario a la lista filtrada
                if user.age == age:
                    filtered_users.append(user)
            # Si no se proporcionan ni el nombre, el correo electrónico ni la edad, se agrega el usuario a la lista filtrada
            else:
                filtered_users.append(user)
        # Devolver la lista de usuarios filtrados
        return filtered_users

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



