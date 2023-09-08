from datetime import timedelta
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.crud.crud_user import crud_user
from app.db.session import sessionmaker
from dotenv import load_dotenv
from app.main import app
from app.api.v1.dependencies import create_access_token, get_db
from app.db.base_class import Base
import os
import pytest
from fastapi.security import HTTPAuthorizationCredentials

from app.schemas.user import User as UserSchema
from app.models.user import User as UserModel

load_dotenv()

engine = create_engine(os.getenv("TEST_DATABASE_URL"))

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db() -> Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield from override_get_db()


@pytest.fixture(scope="function")
def client() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def valid_user() -> Generator:
    email = "test@test.com"
    name = "test"
    password = "test"
    yield UserSchema(name=name, email=email, password=password)


@pytest.fixture(scope="function")
def valid_user_model(db: Session, valid_user: UserSchema) -> Generator:
    user = crud_user.create(db, valid_user)
    yield user


@pytest.fixture(scope="function")
def valid_jwt(valid_user_model: UserModel) -> Generator:
    data = valid_user_model.as_dict()
    token = create_access_token(data, timedelta(minutes=5))
    yield token


@pytest.fixture(scope="function")
def auth_bearer(valid_jwt: str) -> Generator:
    yield HTTPAuthorizationCredentials(scheme="Bearer", credentials=valid_jwt)


@pytest.fixture(scope="function")
def auth_bearer_with_invalid_token() -> Generator:
    yield HTTPAuthorizationCredentials(scheme="Bearer", credentials="invalid-token")
