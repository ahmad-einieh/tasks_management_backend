from fastapi import APIRouter, Response
import CRUD as crud
from models import Task
import time

taskRouter = APIRouter()


@taskRouter.post("/create_task")
async def create_task(res: Response, task: Task):
    try:
        if task.created_at is None:
            task.created_at = time.time()
        crud.create_task(task)
        return {"message": "task created successfully"}
    except:
        res.status_code = 400
        return {"message": "can not create task"}


@taskRouter.delete("/delete_task")
async def delete_task(res: Response, taskId: str):
    try:
        crud.delete_task(taskId)
        return {"message": "task deleted successfully"}
    except:
        res.status_code = 400
        return {"message": "can not delete task"}


@taskRouter.get("/get_all_tasks")
async def get_all_tasks(res: Response, userId: str):
    try:
        return crud.get_tasks_by_user_id(userId)
    except:
        res.status_code = 400
        return {"message": "can not get tasks"}


@taskRouter.get("/get_task")
async def get_task(res: Response, taskId: str):
    try:
        task = crud.get_task(taskId)
        if task:
            return task
        res.status_code = 404
        return {"message": "task not found"}
    except:
        res.status_code = 404
        return {"message": "error on get task"}
    
import traceback

@taskRouter.put("/update_task_complete")
async def update_task_complete(res: Response, taskId: str, isComplete: bool):
    try:
        crud.update_complete_task(taskId, isComplete)
        return {"message": "task updated successfully"}
    except:
        res.status_code = 400
        return {"message": "can not update task"}


# @taskRouter.put("/update_task")
# async def update_task(res:Response,taskId: str, updated_task: Task):
#     try:
#         value = crud.update_task(taskId,updated_task)
#         if value:
#             return {"message":"task updated successfully"}
#         res.status_code = 404
#         return {"message":"task not found"}
#     except:
#         res.status_code = 400
#         return {"message":"can not update task"}
