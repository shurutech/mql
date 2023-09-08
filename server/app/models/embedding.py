import uuid
from sqlalchemy import UUID
from sqlalchemy.orm import mapped_column
from app.models.timestamp_base import TimestampBase
from pgvector.sqlalchemy import Vector


class Embedding(TimestampBase):
    __tablename__ = "embeddings"
    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    embeddings_vector = mapped_column(Vector, nullable=False)
    database_table_id = mapped_column(UUID, nullable=False)
    user_database_id = mapped_column(UUID, nullable=False)

    def as_dict(self) -> dict:
        return {
            "id": str(self.id),
            "embeddings_vector": self.embeddings_vector,
            "database_table_id": str(self.database_table_id),
            "user_database_id": str(self.user_database_id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
