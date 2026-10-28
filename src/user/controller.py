from src.user.dtos import UserSchema, UserLoginSchema
from sqlalchemy.orm import Session
from src.user.model import UserModel
from fastapi import HTTPException, status
from pwdlib import PasswordHash
import jwt
from src.utills.settings import settings
from datetime import datetime, timedelta


password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body:UserSchema, db:Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail = "User already exist...")

    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail = "Email Adddress already exist...")


    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email,  
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    
    return new_user

def login_user(body:UserLoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have enter wrong username")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have enter wrong password")

    exp_time = datetime.now() + timedelta(minutes=settings.EXPIRES_IN_MINUTES)

    token  = jwt.encode({"_id":user.id, "exp":exp_time},settings.SECRET_KEY, settings.ALGORITHM)

    return {"token":token}