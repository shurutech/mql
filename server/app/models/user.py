import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column
from app.models.timestamp_base import TimestampBase


class User(TimestampBase):
    __tablename__ = "users"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    hashed_password = mapped_column(String, nullable=False)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
