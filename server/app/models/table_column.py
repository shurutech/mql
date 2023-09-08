import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column

from app.models.timestamp_base import TimestampBase


class TableColumn(TimestampBase):
    __tablename__ = "table_columns"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    name = mapped_column(String, nullable=False)
    data_type = mapped_column(String, nullable=False)
    database_table_id = mapped_column(UUID, nullable=False)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "data_type": self.data_type,
            "database_table_id": str(self.database_table_id),
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
