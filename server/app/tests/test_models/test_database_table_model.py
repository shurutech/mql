import uuid
from sqlalchemy.orm import Session
from app.models.database_table import DatabaseTable


def test_as_dict_method_with_not_null_text_node(db: Session) -> None:
    user_database_id = uuid.uuid4()
    database_table_instance = DatabaseTable(
        name="test_table", text_node="text_node", user_database_id=user_database_id
    )
    db.add(database_table_instance)
    db.commit()
    result = database_table_instance.as_dict()
    assert "id" in result
    assert isinstance(result["id"], str)
    assert isinstance(result["user_database_id"], str)
    assert result == {
        "name": "test_table",
        "user_database_id": str(user_database_id),
        "id": result["id"],
        "text_node": "text_node",
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
    }


def test_as_dict_method_with_null_text_node(db: Session) -> None:
    user_database_id = uuid.uuid4()
    database_table_instance = DatabaseTable(
        name="test_table", user_database_id=user_database_id
    )
    db.add(database_table_instance)
    db.commit()
    result = database_table_instance.as_dict()
    assert "id" in result
    assert isinstance(result["id"], str)
    assert result == {
        "name": "test_table",
        "user_database_id": str(user_database_id),
        "id": result["id"],
        "text_node": None,
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
    }


def test_timestamp_on_create(db: Session) -> None:
    user_database_id = uuid.uuid4()
    database_table_instance = DatabaseTable(
        name="test_table", user_database_id=user_database_id
    )
    db.add(database_table_instance)
    db.commit()
    assert database_table_instance.created_at is not None
    assert database_table_instance.updated_at is not None
    assert database_table_instance.created_at == database_table_instance.updated_at


def test_timestamp_on_update(db: Session) -> None:
    user_database_id = uuid.uuid4()
    database_table_instance = DatabaseTable(
        name="test_table", user_database_id=user_database_id
    )
    db.add(database_table_instance)
    db.commit()
    database_table_instance.name = "test_table_updated"
    db.commit()
    assert database_table_instance.created_at is not None
    assert database_table_instance.updated_at is not None
    assert database_table_instance.created_at != database_table_instance.updated_at
