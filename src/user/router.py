from fastapi import APIRouter, Depends, status
from src.user.dtos import UserSchema, UserResponseSchema
from sqlalchemy.orm import Session
from src.utills.db import get_db
from src.user import controller


user_routs = APIRouter(prefix="/user")

@user_routs.post("/register", response_model=UserResponseSchema, status_code = status.HTTP_201_CREATED )
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register(body, db)
