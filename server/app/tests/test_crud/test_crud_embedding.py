from app.crud.crud_embedding import CRUDEmbedding
from uuid import uuid4
from sqlalchemy.orm import Session
from app.schemas.embedding import Embedding as EmbeddingSchema
from app.models.embedding import Embedding as EmbeddingModel


def test_create_embedding(db: Session) -> None:
    crud_embedding = CRUDEmbedding()
    embedding_obj = EmbeddingSchema(
        embeddings_vector=[1, 2, 3, 4, 5],
        database_table_id=uuid4(),
        user_database_id=uuid4(),
    )

    result = crud_embedding.create(db=db, embedding_obj=embedding_obj)

    assert result is not None
    assert result.embeddings_vector is not None
    assert result.database_table_id == embedding_obj.database_table_id
    assert result.user_database_id == embedding_obj.user_database_id
    assert (
        db.query(EmbeddingModel).filter(EmbeddingModel.id == result.id).first()
        is not None
    )


def test_get_closest_embeddings_by_database_id(db: Session) -> None:
    crud_embedding = CRUDEmbedding()
    embedding_obj = EmbeddingSchema(
        embeddings_vector=[1, 2, 3, 4, 5],
        database_table_id=uuid4(),
        user_database_id=uuid4(),
    )
    result = crud_embedding.create(db=db, embedding_obj=embedding_obj)

    result = crud_embedding.get_closest_embeddings_by_database_id(
        query_embedding=[1, 2, 3, 4, 5],
        database_id=embedding_obj.user_database_id,
        db=db,
    )
    assert result is not None

def delete_by_database_id(db: Session) -> None:
    crud_embedding = CRUDEmbedding()
    embedding_obj = EmbeddingSchema(
        embeddings_vector=[1, 2, 3, 4, 5],
        database_table_id=uuid4(),
        user_database_id=uuid4(),
    )
    result = crud_embedding.create(db=db, embedding_obj=embedding_obj)

    crud_embedding.delete_by_database_id(db=db, database_id=embedding_obj.user_database_id)
    result = crud_embedding.get_by_user_database_id(
        db=db, user_database_id=embedding_obj.user_database_id
    )
    assert result.count() == 0
    assert result[0].embeddings_vector == embedding_obj.embeddings_vector
    assert result[0].database_table_id == embedding_obj.database_table_id
    assert result[0].user_database_id == embedding_obj.user_database_id
    assert (
        db.query(EmbeddingModel).filter(EmbeddingModel.id == result[0].id).first()
        is not None
    )