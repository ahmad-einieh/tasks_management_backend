from fastapi import APIRouter
import CRUD as crud
from models import User

tastRouter = APIRouter()

@tastRouter.get("/get_task")
async def get_task(taskId: str):
    return crud.get_task(taskId)

@tastRouter.post("/create_task")
async def create_task(task: User):
    return crud.create_task(task)

@tastRouter.put("/update_task")
async def update_task(taskId: str, updated_task: User):
    return crud.update_task(taskId, updated_task)

@tastRouter.delete("/delete_task")
async def delete_task(taskId: str):
    return crud.delete_task(taskId)

@tastRouter.get("/get_all_tasks")
async def get_all_tasks(userId: str):
    return crud.get_tasks_by_user_id(userId)