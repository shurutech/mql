import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column
from app.models.timestamp_base import TimestampBase


class UserDatabase(TimestampBase):
    __tablename__ = "user_databases"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    name = mapped_column(String, nullable=False)
    user_id = mapped_column(UUID, nullable=False)
    connection_string = mapped_column(String, nullable=True)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "user_id": str(self.user_id),
            "connection_string": self.connection_string,
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
