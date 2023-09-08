from uuid import uuid4
from pydantic import ValidationError
import pytest
from app.schemas.embedding import Embedding as EmbeddingSchema


def test_embedding_schema_with_valid_data():
    id = uuid4()
    database_table_id = uuid4()
    user_database_id = uuid4()
    embedding_vector = [1.0, 2.3, 3.5]
    valid_embedding = EmbeddingSchema(
        id=id,
        embeddings_vector=embedding_vector,
        database_table_id=database_table_id,
        user_database_id=user_database_id,
    )

    assert valid_embedding.id == id
    assert valid_embedding.embeddings_vector == embedding_vector
    assert valid_embedding.database_table_id == database_table_id
    assert valid_embedding.user_database_id == user_database_id


def test_embedding_schema_with_missing_id():
    database_table_id = uuid4()
    user_database_id = uuid4()
    embedding_vector = [1.0, 2.3, 3.5]
    valid_embedding = EmbeddingSchema(
        embeddings_vector=embedding_vector,
        database_table_id=database_table_id,
        user_database_id=user_database_id,
    )

    assert valid_embedding.embeddings_vector == embedding_vector
    assert valid_embedding.database_table_id == database_table_id
    assert valid_embedding.user_database_id == user_database_id
    assert valid_embedding.id is None


def test_embedding_schema_with_missing_database_table_id():
    id = uuid4()
    user_database_id = uuid4()
    embedding_vector = [1.0, 2.3, 3.5]

    with pytest.raises(ValidationError):
        EmbeddingSchema(
            id=id, embeddings_vector=embedding_vector, user_database_id=user_database_id
        )


def test_embedding_schema_with_missing_user_database_id():
    id = uuid4()
    database_table_id = uuid4()
    embedding_vector = [1.0, 2.3, 3.5]

    with pytest.raises(ValidationError):
        EmbeddingSchema(
            id=id,
            embeddings_vector=embedding_vector,
            database_table_id=database_table_id,
        )


def test_embedding_schema_with_missing_embedding():
    id = uuid4()
    database_table_id = uuid4()
    user_database_id = uuid4()

    with pytest.raises(ValidationError):
        EmbeddingSchema(
            id=id,
            database_table_id=database_table_id,
            user_database_id=user_database_id,
        )


def test_embedding_schema_with_invalid_embedding():
    id = uuid4()
    database_table_id = uuid4()
    user_database_id = uuid4()
    embeddings_vector = "invalid_embedding"

    with pytest.raises(ValidationError):
        EmbeddingSchema(
            id=id,
            embeddings_vector=embeddings_vector,
            database_table_id=database_table_id,
            user_database_id=user_database_id,
        )
