from fastapi import APIRouter, Form, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db, create_access_token
from app.crud.crud_user import crud_user
from app.schemas.user import User
from datetime import timedelta
import logging


router = APIRouter()
logger = logging.getLogger("analytics")


@router.post("/signup")
async def signup(
    name: Annotated[str, Form()],
    email: Annotated[EmailStr, Form()],
    password: Annotated[str, Form()],
    db: Session = Depends(get_db),
) -> JSONResponse:
    try:
        user = crud_user.get_by_email(db, email)
        if user:
            logger.info("User already exists with email {}".format(email))
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User Already Exists"
            )

        user = crud_user.create(db, User(name=name, email=email, password=password))
        if not user:
            logger.error("User not created for email {}".format(email))
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
        token = create_access_token(
            data={"id": str(user.id), "email": user.email, "name": user.name},
            expires_delta=timedelta(minutes=60),
        )
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error("User creation failed for email {}. Error is {}".format(email, e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
    return JSONResponse(
        content={
            "message": "User created successfully",
            "data": {"name": user.name, "email": user.email},
        },
        headers={"x-auth-token": token},
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/login")
async def login(
    email: Annotated[EmailStr, Form()],
    password: Annotated[str, Form()],
    db: Session = Depends(get_db),
) -> JSONResponse:
    try:
        user = crud_user.get_by_email(db, email)
        if not user:
            logger.info("User not found for email {}".format(email))
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
            )
        if not crud_user.authenticate(db, email, password):
            logger.info("Incorrect password for email {}".format(email))
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password"
            )
        token = create_access_token(
            data={"id": str(user.id), "email": user.email, "name": user.name},
            expires_delta=timedelta(minutes=60),
        )
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error("User login failed for email {}. Error is {}".format(email, e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Login successfully",
            "data": {"name": user.name, "email": user.email},
        },
        headers={"x-auth-token": token},
        status_code=status.HTTP_200_OK,
    )
