from fastapi import APIRouter, Response, status, HTTPException, Header
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
encryptFunction = Fernet(key)
user = APIRouter()

validToken = "fastApiToken"

@user.get("/users", tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id:int, x_token:str = Header()):
    if x_token != validToken:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    response = conn.execute(users.select().where(users.c.id == id)).first()
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")
    return response

@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = {"id":user.id, "name": user.name, "email":user.email, "password":user.password}
    conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == user.id)).first()

@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id:int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id:int, user:User):
    conn.execute(users.update().values(name = user.name, email = user.email, password = encryptFunction.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.get("/api")
def say_hello():
    return {"message":"hello world"}