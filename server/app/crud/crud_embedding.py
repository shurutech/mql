from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.embedding import Embedding as EmbeddingModel
from app.schemas.embedding import Embedding as EmbeddingSchema


class CRUDEmbedding:
    def create(self, db: Session, embedding_obj: EmbeddingSchema) -> EmbeddingModel:
        embedding = EmbeddingModel(
            embeddings_vector=embedding_obj.embeddings_vector,
            database_table_id=embedding_obj.database_table_id,
            user_database_id=embedding_obj.user_database_id,
        )
        db.add(embedding)
        db.commit()
        db.refresh(embedding)
        return embedding

    def get_by_user_database_id(
        self, db: Session, user_database_id: UUID
    ) -> List[EmbeddingModel]:
        return db.query(EmbeddingModel).filter(
            EmbeddingModel.user_database_id == user_database_id
        )

    def get_closest_embeddings_by_database_id(
        self, query_embedding: list[float], database_id: UUID, db: Session
    ) -> List[str]:
        return (
            db.query(EmbeddingModel.database_table_id)
            .filter(EmbeddingModel.user_database_id == database_id)
            .order_by(EmbeddingModel.embeddings_vector.l2_distance(query_embedding))
            .limit(5)
        )
    
    def delete_by_database_id(self, db: Session, database_id: UUID) -> None:
        db.query(EmbeddingModel).filter(EmbeddingModel.user_database_id == database_id).delete()


crud_embedding = CRUDEmbedding()
