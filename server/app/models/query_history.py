import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column
from app.models.timestamp_base import TimestampBase


class QueryHistory(TimestampBase):
    __tablename__ = "query_histories"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    nl_query = mapped_column(String, nullable=False)
    sql_query = mapped_column(String, nullable=True)
    user_database_id = mapped_column(UUID, nullable=False)

    def as_dict(self) -> dict:
        return {
            "nl_query": self.nl_query,
            "sql_query": self.sql_query,
            "user_database_id": str(self.user_database_id),
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
