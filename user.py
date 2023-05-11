from fastapi import APIRouter, Response
import CRUD as crud
from models import User
import time
import hashing as hash

userRouter = APIRouter()

@userRouter.get("/get_user")
async def get_user(response:Response, userId: str):
    try:
        return crud.get_user(userId)
    except:
        response.status_code = 404
        return {"message":"user not found"}


@userRouter.post("/create_user")
async def create_user(res:Response, user: User):
    if crud.get_user_by_email(user.email):
        res.status_code = 408
        return {"message":"user already exists"}

    try:
        user.created_at = time.time()
        user.password = hash.encrypt(user.password)
        crud.create_user(user)
        return {"message":"user created successfully"}
    except:
        res.status_code = 400
        return {"message":"can not create user"}


# @userRouter.put("/update_user")
# async def update_user(userId: str, updated_user: User):
#     return crud.update_user(userId, updated_user)

# @userRouter.delete("/delete_user")
# async def delete_user(userId: str):
#     return crud.delete_user(userId)
