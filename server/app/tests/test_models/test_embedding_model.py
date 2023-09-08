import uuid
from sqlalchemy.orm import Session
from app.models.embedding import Embedding


def test_as_dict_method(db: Session) -> None:
    embedding_id = uuid.uuid4()
    table_id = uuid.uuid4()
    database_id = uuid.uuid4()
    embedding_instance = Embedding(
        id=embedding_id,
        embeddings_vector=[1.0, 2.0, 3.0],
        database_table_id=table_id,
        user_database_id=database_id,
    )

    db.add(embedding_instance)
    db.commit()

    db_result = db.query(Embedding).first()
    assert db_result is not None

    result_dict = db_result.as_dict()
    assert isinstance(result_dict["id"], str)
    assert isinstance(result_dict["database_table_id"], str)
    assert isinstance(result_dict["user_database_id"], str)
    assert result_dict["id"] == str(embedding_id)
    assert list(result_dict["embeddings_vector"]) == [1.0, 2.0, 3.0]
    assert result_dict["database_table_id"] == str(table_id)
    assert result_dict["user_database_id"] == str(database_id)
    assert result_dict["created_at"] == db_result.created_at.isoformat()
    assert result_dict["updated_at"] == db_result.updated_at.isoformat()


def test_timestamp_on_create(db: Session) -> None:
    embedding_id = uuid.uuid4()
    table_id = uuid.uuid4()
    database_id = uuid.uuid4()
    embedding_instance = Embedding(
        id=embedding_id,
        embeddings_vector=[1.0, 2.0, 3.0],
        database_table_id=table_id,
        user_database_id=database_id,
    )

    db.add(embedding_instance)
    db.commit()

    db_result = db.query(Embedding).first()
    assert db_result is not None

    assert db_result.created_at is not None
    assert db_result.updated_at is not None
    assert db_result.created_at == db_result.updated_at


def test_timestamp_on_update(db: Session) -> None:
    embedding_id = uuid.uuid4()
    table_id = uuid.uuid4()
    database_id = uuid.uuid4()
    embedding_instance = Embedding(
        id=embedding_id,
        embeddings_vector=[1.0, 2.0, 3.0],
        database_table_id=table_id,
        user_database_id=database_id,
    )

    db.add(embedding_instance)
    db.commit()

    db_result = db.query(Embedding).first()
    assert db_result is not None

    db_result.embeddings_vector = [4.0, 5.0, 6.0]
    db.commit()

    assert db_result.created_at is not None
    assert db_result.updated_at is not None
    assert db_result.created_at != db_result.updated_at
