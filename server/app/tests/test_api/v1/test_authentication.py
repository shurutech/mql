from fastapi.testclient import TestClient
from app.crud.crud_user import crud_user
from app.schemas.user import User as UserSchema
from sqlalchemy.orm import Session


def test_login_user(client: TestClient, db: Session, valid_user: UserSchema) -> None:
    crud_user.create(db, valid_user)
    response = client.post(
        "/api/v1/login",
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
        "/api/v1/login",
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
        "/api/v1/login",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"email": valid_user.email, "password": "wrong"},
    )
    assert response.status_code == 401
    assert response.headers.get("x-auth-token") is None
    assert response.json() == {"detail": "Incorrect Password"}
