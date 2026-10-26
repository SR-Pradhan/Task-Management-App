from fastapi import APIRouter, Depends, status
from src.task import controller
from src.task.dtos import TaskSchema
from src.utills.db import get_db


task_routers = APIRouter(prefix="/task")

@task_routers.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_routers.get("/all_task", status_code=status.HTTP_200_OK)
def get_all_task(db = Depends(get_db)):
    return controller.get_tasks(db)

@task_routers.get("/one_task/{task_id}", status_code=status.HTTP_200_OK)
def get_one_task(task_id:int, db = Depends(get_db)):
    return controller.get_one_task(task_id, db)

@task_routers.put("/update_task/{task_id}", status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema, task_id:int, db = Depends(get_db)):
    return controller.update_task(body, task_id, db)

@task_routers.delete("/delete_task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db = Depends(get_db)):
    return controller.delete_task(task_id, db)
