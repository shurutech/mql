import uuid
from sqlalchemy.orm import Session
from app.models.user_database import UserDatabase


def test_as_dict_method(db: Session) -> None:
    user_id = uuid.uuid4()
    user_database_instance = UserDatabase(name="test_database", user_id=user_id)
    db.add(user_database_instance)
    db.commit()
    result = user_database_instance.as_dict()

    assert "id" in result
    assert isinstance(result["id"], str)
    assert isinstance(result["user_id"], str)
    assert result == {
        "name": "test_database",
        "user_id": str(user_id),
        "id": result["id"],
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
    }


def test_timestamp_on_create(db: Session) -> None:
    user_id = uuid.uuid4()
    user_database_instance = UserDatabase(name="test_database", user_id=user_id)

    db.add(user_database_instance)
    db.commit()

    assert user_database_instance.created_at is not None
    assert user_database_instance.updated_at is not None
    assert user_database_instance.created_at == user_database_instance.updated_at


def test_timestamp_on_update(db: Session) -> None:
    user_id = uuid.uuid4()
    user_database_instance = UserDatabase(name="test_database", user_id=user_id)

    db.add(user_database_instance)
    db.commit()
    user_database_instance.name = "test_database_updated"
    db.commit()
    assert user_database_instance.created_at is not None
    assert user_database_instance.updated_at is not None
    assert user_database_instance.created_at != user_database_instance.updated_at
