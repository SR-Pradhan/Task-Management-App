from fastapi import FastAPI
from src.utills.db import Base, engine
from src.task.router import task_routers
#from src.task.model import TaskModel

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(task_routers)