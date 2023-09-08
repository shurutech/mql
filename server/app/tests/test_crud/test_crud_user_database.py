import uuid
from sqlalchemy.orm import Session
from app.crud.crud_user_database import CRUDUserDatabase
from app.schemas.user_database import UserDatabase as UserDatabaseSchema
from app.models.user_database import UserDatabase as UserDatabaseModel


def test_create_user_database(db: Session) -> None:
    crud_user_database = CRUDUserDatabase()
    user_database_obj = UserDatabaseSchema(name="test_database", user_id=uuid.uuid4())

    result = crud_user_database.create(db=db, user_database_obj=user_database_obj)

    assert result.name == user_database_obj.name
    assert result.user_id == user_database_obj.user_id
    assert (
        db.query(UserDatabaseModel).filter(UserDatabaseModel.id == result.id).first()
        is not None
    )


def test_get_by_user_id(db: Session) -> None:
    crud_user_database = CRUDUserDatabase()
    user_database_obj = UserDatabaseSchema(name="test_database", user_id=uuid.uuid4())
    crud_user_database.create(db=db, user_database_obj=user_database_obj)

    result = crud_user_database.get_by_user_id(db=db, user_id=user_database_obj.user_id)

    assert result.count() == 1
    assert result[0].name == user_database_obj.name
    assert result[0].user_id == user_database_obj.user_id
    assert (
        db.query(UserDatabaseModel).filter(UserDatabaseModel.id == result[0].id).first()
        is not None
    )


def test_get_by_user_id_not_found(db: Session) -> None:
    crud_user_database = CRUDUserDatabase()
    user_database_obj = UserDatabaseSchema(name="test_database", user_id=uuid.uuid4())
    crud_user_database.create(db=db, user_database_obj=user_database_obj)

    result = crud_user_database.get_by_user_id(db=db, user_id=uuid.uuid4())

    assert result.count() == 0


def test_get_by_id(db: Session) -> None:
    crud_user_database = CRUDUserDatabase()
    user_database_obj = UserDatabaseSchema(name="test_database", user_id=uuid.uuid4())
    user_database = crud_user_database.create(
        db=db, user_database_obj=user_database_obj
    )

    result = crud_user_database.get_by_id(db=db, id=user_database.id)

    assert result is not None
    assert result.name == user_database_obj.name
    assert result.user_id == user_database_obj.user_id
    assert result.id == user_database.id
    assert (
        db.query(UserDatabaseModel).filter(UserDatabaseModel.id == result.id).first()
        is not None
    )
