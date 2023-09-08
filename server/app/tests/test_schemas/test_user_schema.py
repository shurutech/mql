import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.user import User as UserSchema


def test_user_schema_with_valid_data(valid_user: UserSchema) -> None:
    id = uuid4()
    user = UserSchema(
        id=id,
        name=valid_user.name,
        email=valid_user.email,
        password=valid_user.password,
    )

    assert user.id == id
    assert user.name == valid_user.name
    assert user.email == valid_user.email
    assert user.password == valid_user.password


def test_user_schema_with_missing_id(valid_user: UserSchema) -> None:
    user = UserSchema(
        name=valid_user.name, email=valid_user.email, password=valid_user.password
    )

    assert user.name == valid_user.name
    assert user.email == valid_user.email
    assert user.password == valid_user.password
    assert user.id is None


def test_user_schema_with_missing_name(valid_user: UserSchema) -> None:
    with pytest.raises(ValidationError):
        UserSchema(name=None, email=valid_user.email, password=valid_user.password)


def test_user_schema_with_missing_email(valid_user: UserSchema) -> None:
    with pytest.raises(ValidationError):
        UserSchema(name=valid_user.name, email=None, password=valid_user.password)


def test_user_schema_with_missing_password(valid_user: UserSchema) -> None:
    with pytest.raises(ValidationError):
        UserSchema(name=valid_user.name, email=valid_user.email, password=None)


def test_user_schema_with_invalid_name(valid_user: UserSchema) -> None:
    id = uuid4()
    name = 123

    with pytest.raises(ValidationError):
        UserSchema(
            id=id, name=name, email=valid_user.email, password=valid_user.password
        )


def test_user_schema_with_invalid_email(valid_user: UserSchema) -> None:
    id = uuid4()
    email = "testemail.com"

    with pytest.raises(ValidationError):
        UserSchema(
            id=id, name=valid_user.name, email=email, password=valid_user.password
        )


def test_user_schema_with_invalid_password(valid_user: UserSchema) -> None:
    id = uuid4()
    password = 123

    with pytest.raises(ValidationError):
        UserSchema(
            id=id, name=valid_user.name, email=valid_user.email, password=password
        )


def test_user_schema_with_invalid_user_id(valid_user: UserSchema) -> None:
    id = "invalid_uuid"

    with pytest.raises(ValidationError):
        UserSchema(
            id=id,
            name=valid_user.name,
            email=valid_user.email,
            password=valid_user.password,
        )
