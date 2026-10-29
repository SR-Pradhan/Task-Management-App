from sqlalchemy.orm import Session
from src.user.model import UserModel
from fastapi import HTTPException, status, Request, Depends
import jwt
from src.utills.settings import settings
from jwt.exceptions import InvalidTokenError
from src.utills.db import get_db


def is_authenticated(request:Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthoriased")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthoriased")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthoriased")

