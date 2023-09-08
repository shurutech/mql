import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.user_database import UserDatabase


def test_user_database_schema_with_valid_data() -> None:
    name = "Test Database"
    user_id = uuid4()

    user_database = UserDatabase(name=name, user_id=user_id)

    assert user_database.name == name
    assert user_database.user_id == user_id


def test_user_database_schema_with_missing_name() -> None:
    user_id = uuid4()

    with pytest.raises(ValidationError):
        UserDatabase(name=None, user_id=user_id)


def test_user_database_schema_with_invalid_name() -> None:
    name = 123
    user_id = uuid4()

    with pytest.raises(ValidationError):
        UserDatabase(name=name, user_id=user_id)


def test_user_database_schema_with_missing_user_id() -> None:
    name = "Test Database"

    with pytest.raises(ValidationError):
        UserDatabase(name=name, user_id=None)


def test_user_database_schema_with_invalid_user_id() -> None:
    name = "Test Database"
    user_id = "invalid_uuid"

    with pytest.raises(ValidationError):
        UserDatabase(name=name, user_id=user_id)
