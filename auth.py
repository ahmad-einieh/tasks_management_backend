
from fastapi import HTTPException #,Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional
# import jwt
from fastapi import APIRouter
import CRUD as crud
from models import User
import hashing as hash

SECRET_KEY = "this_is_a_secret_key_for_development"

def verify_user(email: str, password: str) -> Optional[User]:
    db_user = crud.get_user_by_email(email)
    if db_user and hash.verfiy(password, db_user.password):
        return db_user
    return None


# def generate_token(user: User):
#     encoded_data = jwt.encode({"email": user.email,"userId":user.id}, SECRET_KEY, algorithm="HS256") 
#     return encoded_data


# def decode_token(token: str) -> Optional[User]:
#     try:
#         decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         email = decoded_data.get("email")
#         db_user = crud.get_user_by_email(email)
#         if db_user:
#             return User(**db_user)
#         return None
#     except jwt.PyJWTError:
#         return None


authRouter = APIRouter()


@authRouter.post("/login")
def login(email:str, password:str):
    user = verify_user(email, password)
    if user:
        # token = generate_token(user)
        del user.password
        del user.created_at
        return user
    raise HTTPException(status_code=401, detail="Invalid email or password")
