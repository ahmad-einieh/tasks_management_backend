
from fastapi import  Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
from fastapi import APIRouter
import CRUD as crud
from models import User , Token


SECRET_KEY = "this_is_a_secret_key_for_development"

def verify_user(username: str, password: str) -> Optional[User]:
    db_user = crud.get_user(username)
    if db_user and db_user["password"] == password:
        return User(**db_user)
    return None


def generate_token(user: User) -> Token:
    encoded_data = jwt.encode({"email": user.email,"userId":user.id}, SECRET_KEY, algorithm="HS256") 
    return Token(access_token=encoded_data, token_type="bearer")


def decode_token(token: str) -> Optional[User]:
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = decoded_data.get("username")
        db_user = crud.get_user(username)
        if db_user:
            return User(**db_user)
        return None
    except jwt.PyJWTError:
        return None


authRouter = APIRouter()


@authRouter.post(response_model=Token)
def login(email:str, password:str):
    user = verify_user(email, password)
    if user:
        token = generate_token(user)
        return token
    raise HTTPException(status_code=401, detail="Invalid username or password")
