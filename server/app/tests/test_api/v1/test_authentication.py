from fastapi.testclient import TestClient
from app.crud.crud_user import crud_user
from app.schemas.user import User as UserSchema
from sqlalchemy.orm import Session


def test_signup_new_user(client: TestClient, valid_user: UserSchema) -> None:
    response = client.post(
        "/v1/signup",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "name": valid_user.name,
            "email": valid_user.email,
            "password": valid_user.password,
        },
    )
    assert response.status_code == 201
    assert response.headers["x-auth-token"] is not None
    assert response.json() == {
        "message": "User created successfully",
        "data": {"name": valid_user.name, "email": valid_user.email}
        }


def test_signup_user_already_exists(
    client: TestClient, db: Session, valid_user: UserSchema
) -> None:
    crud_user.create(db, valid_user)
    response = client.post(
        "/v1/signup",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "name": valid_user.name,
            "email": valid_user.email,
            "password": valid_user.password,
        },
    )
    assert response.status_code == 400
    assert response.headers.get("x-auth-token") is None
    assert response.json() == {"detail": "User Already Exists"}


def test_login_user(client: TestClient, db: Session, valid_user: UserSchema) -> None:
    crud_user.create(db, valid_user)
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"email": valid_user.email, "password": valid_user.password},
    )
    assert response.status_code == 200
    assert response.headers["x-auth-token"] is not None
    assert response.json() == {
        "message": "Login successfully",
        "data": {"name": valid_user.name, "email": valid_user.email}
        }


def test_login_user_not_found(client: TestClient, valid_user: UserSchema) -> None:
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"email": valid_user.email, "password": valid_user.password},
    )
    assert response.status_code == 404
    assert response.headers.get("x-auth-token") is None
    assert response.json() == {"detail": "User Not Found"}


def test_login_user_incorrect_password(
    client: TestClient, db: Session, valid_user: UserSchema
) -> None:
    crud_user.create(db, valid_user)
    response = client.post(
        "/v1/login",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"email": valid_user.email, "password": "wrong"},
    )
    assert response.status_code == 401
    assert response.headers.get("x-auth-token") is None
    assert response.json() == {"detail": "Incorrect Password"}
