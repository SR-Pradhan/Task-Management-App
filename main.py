from fastapi import FastAPI
from src.utills.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()