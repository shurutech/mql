import uuid
from sqlalchemy import String, UUID, Text
from sqlalchemy.orm import mapped_column
from app.models.timestamp_base import TimestampBase


class DatabaseTable(TimestampBase):
    __tablename__ = "database_tables"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    name = mapped_column(String, nullable=False)
    text_node = mapped_column(Text, nullable=True)
    user_database_id = mapped_column(UUID, nullable=False)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "user_database_id": str(self.user_database_id),
            "id": str(self.id),
            "text_node": self.text_node,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
