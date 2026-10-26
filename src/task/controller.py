from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.model import TaskModel
from fastapi import HTTPException


def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], 
                         description = data["description"],
                         is_completed = data["is_completed"]
                         )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)




    return{"status":"Task Created Successfully...", "data":new_task}


def get_tasks(db:Session):
    task = db.query(TaskModel).all()
    return {"status":"All Tasks", "dats":task}

def get_one_task(task_id:int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "Task id is Incorrect")
    
    return{"status":"Task fatched successfully", "data":one_task}

def update_task(body:TaskSchema, task_id:int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "Task id is Incorrect")


    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return {"ststus":"Task Updated Successfully...", "data":one_task}


def delete_task(task_id:int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail = "Task id is Incorrect")

    db.delete(one_task)
    db.commit()

    return None

