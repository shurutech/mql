from uuid import UUID
from pydantic import BaseModel, ConfigDict


class TableColumn(BaseModel):
    name: str
    data_type: str
    database_table_id: UUID

    model_config = ConfigDict(from_attributes=True)
