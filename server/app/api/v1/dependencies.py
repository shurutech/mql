from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.crud.crud_user import crud_user
from app.db.session import sessionLocal
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
import os

load_dotenv()


def get_db() -> Generator:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt


def validate_access_token(token: str) -> dict | bool:
    try:
        payload = jwt.decode(
            token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")]
        )
        return payload
    except ExpiredSignatureError:
        return False
    except JWTError:
        return False


def get_current_user(
    credentials: str = Depends(HTTPBearer()), db: Session = Depends(get_db)
) -> UserModel:
    payload = validate_access_token(credentials.credentials)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )
    user = crud_user.get_by_email(db, payload["email"])
    user.hashed_key = payload["hashed_key"]
    return user
