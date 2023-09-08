import os
import uuid
import pytest
from jose import jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import timedelta, datetime
from fastapi.security import HTTPAuthorizationCredentials
from app.models.user import User as UserModel
from app.api.v1.dependencies import (
    validate_access_token,
    get_current_user,
)


def is_valid_uuid(id_to_test) -> bool:
    try:
        uuid.UUID(str(id_to_test))
        return True
    except ValueError:
        return False


def test_validate_access_token_with_valid_token(
    valid_user_model: UserModel, valid_jwt: str
) -> None:
    payload = validate_access_token(valid_jwt)
    assert payload["name"] == valid_user_model.name
    assert payload["email"] == valid_user_model.email


def test_validate_access_token_with_expired_token() -> None:
    expired_data = {
        "name": "test",
        "email": "test@test.com",
        "exp": datetime.utcnow() - timedelta(minutes=30),
    }
    expired_token = jwt.encode(
        expired_data, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    expired_payload = validate_access_token(expired_token)
    assert expired_payload is False


def test_validate_access_token_with_invalid_token() -> None:
    invalid_token = "this-is-not-a-valid-token"
    invalid_payload = validate_access_token(invalid_token)
    assert invalid_payload is False


def test_get_current_user_with_valid_token(
    valid_user_model: UserModel, auth_bearer: HTTPAuthorizationCredentials, db: Session
) -> None:
    user = get_current_user(auth_bearer, db)
    assert user.name == valid_user_model.name
    assert user.email == valid_user_model.email
    assert is_valid_uuid(user.id)


def test_get_current_user_with_invalid_token(
    auth_bearer_with_invalid_token: HTTPAuthorizationCredentials, db: Session
) -> None:
    with pytest.raises(HTTPException) as e:
        get_current_user(auth_bearer_with_invalid_token, db)
    assert e.value.status_code == 401
    assert e.value.detail == "Invalid Token"
