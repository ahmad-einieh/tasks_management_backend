from fastapi import APIRouter, Response
import CRUD as crud
from models import  Task, TaskUpdate
import time

taskRouter = APIRouter()

@taskRouter.get("/get_task")
async def get_task(res:Response, taskId: str):
    try:
        return crud.get_task(taskId)
    except:
        res.status_code = 404
        return {"message":"task not found"}


@taskRouter.post("/create_task")
async def create_task(res:Response,task: Task):
    try:
        if task.length:
            task.created_at = time.time()
            task.end_at = task.created_at + task.length
        else:
            task.created_at = time.time()
        crud.create_task(task)
        return {"message":"task created successfully"}
    except:
        res.status_code = 400
        return {"message":"can not create task"}


@taskRouter.put("/update_task")
async def update_task(res:Response,taskId: str, updated_task: TaskUpdate):
    try:
        old_task = crud.get_task(taskId)
        if updated_task.add_length:
            old_task.length += updated_task.add_length

        if updated_task.title:
            old_task.title = updated_task.title
        if updated_task.description:
            old_task.description = updated_task.description
        if updated_task.isComplete:
            old_task.isComplete = updated_task.isComplete
        if updated_task.category:
            old_task.category = updated_task.category
        if updated_task.tags:
            old_task.tags = updated_task.tags

        crud.update_task(taskId, old_task)
        return {"message":"task updated successfully"}
    except:
        res.status_code = 400
        return {"message":"can not update task"}

@taskRouter.delete("/delete_task")
async def delete_task(res:Response,taskId: str):
    try:
        crud.delete_task(taskId)
        return {"message":"task deleted successfully"}
    except:
        res.status_code = 400
        return {"message":"can not delete task"}

@taskRouter.get("/get_all_tasks")
async def get_all_tasks(res:Response,userId: str):
    try:
        return crud.get_tasks_by_user_id(userId)
    except:
        res.status_code = 400
        return {"message":"can not get tasks"}