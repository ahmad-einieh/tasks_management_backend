from fastapi import APIRouter
import CRUD as crud
from models import User

taskRouter = APIRouter()

@taskRouter.get("/get_task")
async def get_task(taskId: str):
    return crud.get_task(taskId)

@taskRouter.post("/create_task")
async def create_task(task: User):
    return crud.create_task(task)

@taskRouter.put("/update_task")
async def update_task(taskId: str, updated_task: User):
    return crud.update_task(taskId, updated_task)

@taskRouter.delete("/delete_task")
async def delete_task(taskId: str):
    return crud.delete_task(taskId)

@taskRouter.get("/get_all_tasks")
async def get_all_tasks(userId: str):
    return crud.get_tasks_by_user_id(userId)