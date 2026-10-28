from fastapi import FastAPI
from src.utills.db import Base, engine
from src.task.router import task_routers
from src.user.router import user_routs


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(task_routers)
app.include_router(user_routs)
