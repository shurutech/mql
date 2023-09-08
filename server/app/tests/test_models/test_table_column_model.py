import uuid
from sqlalchemy.orm import Session
from app.models.table_column import TableColumn


def test_as_dict_method(db: Session) -> None:
    database_table_id = uuid.uuid4()
    table_column_instance = TableColumn(
        name="test_column",
        data_type="Character Varying",
        database_table_id=database_table_id,
    )
    db.add(table_column_instance)
    db.commit()
    result = table_column_instance.as_dict()
    assert "id" in result
    assert isinstance(result["id"], str)
    assert isinstance(result["database_table_id"], str)
    assert result == {
        "name": "test_column",
        "data_type": "Character Varying",
        "database_table_id": str(database_table_id),
        "id": result["id"],
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
    }


def test_timestamp_on_create(db: Session) -> None:
    database_table_id = uuid.uuid4()
    table_column_instance = TableColumn(
        name="test_column",
        data_type="Character Varying",
        database_table_id=database_table_id,
    )
    db.add(table_column_instance)
    db.commit()
    assert table_column_instance.created_at is not None
    assert table_column_instance.updated_at is not None
    assert table_column_instance.created_at == table_column_instance.updated_at


def test_timestamp_on_update(db: Session) -> None:
    database_table_id = uuid.uuid4()
    table_column_instance = TableColumn(
        name="test_column",
        data_type="Character Varying",
        database_table_id=database_table_id,
    )
    db.add(table_column_instance)
    db.commit()
    table_column_instance.name = "test_column_updated"
    db.commit()
    assert table_column_instance.created_at is not None
    assert table_column_instance.updated_at is not None
    assert table_column_instance.created_at != table_column_instance.updated_at
