import uuid
from sqlalchemy.orm import Session
from app.models.query_history import QueryHistory


def test_as_dict_method(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_instance = QueryHistory(
        nl_query="test_nl_query",
        sql_query="test_sql_query",
        user_database_id=user_database_id,
    )
    db.add(query_history_instance)
    db.commit()
    result = query_history_instance.as_dict()

    assert "id" in result
    assert isinstance(result["id"], str)
    assert isinstance(result["user_database_id"], str)
    assert result == {
        "nl_query": "test_nl_query",
        "sql_query": "test_sql_query",
        "user_database_id": str(user_database_id),
        "id": result["id"],
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
    }


def test_timestamp_on_create(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_instance = QueryHistory(
        nl_query="test_nl_query",
        sql_query="test_sql_query",
        user_database_id=user_database_id,
    )

    db.add(query_history_instance)
    db.commit()

    assert query_history_instance.created_at is not None
    assert query_history_instance.updated_at is not None
    assert query_history_instance.created_at == query_history_instance.updated_at


def test_timestamp_on_update(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_instance = QueryHistory(
        nl_query="test_nl_query",
        sql_query="test_sql_query",
        user_database_id=user_database_id,
    )
    db.add(query_history_instance)
    db.commit()
    query_history_instance.nl_query = "test_nl_query_updated"
    db.commit()
    assert query_history_instance.created_at is not None
    assert query_history_instance.updated_at is not None
    assert query_history_instance.created_at != query_history_instance.updated_at
