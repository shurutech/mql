from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class DatabaseTable(BaseModel):
    name: str
    user_database_id: UUID
    text_node: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
