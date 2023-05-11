from fastapi import APIRouter
import CRUD as crud
from models import User
import time

userRouter = APIRouter()

@userRouter.get("/get_user")
async def get_user(userId: str):
    return crud.get_user(userId)

@userRouter.post("/create_user")
async def create_user(user: User):
    user.created_at = time.time()
    return crud.create_user(user)

@userRouter.put("/update_user")
async def update_user(userId: str, updated_user: User):
    return crud.update_user(userId, updated_user)

@userRouter.delete("/delete_user")
async def delete_user(userId: str):
    return crud.delete_user(userId)
