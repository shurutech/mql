from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class Query(BaseModel):
    id: Optional[UUID] = None
    nl_query: str
    sql_query: Optional[str] = None
    user_database_id: UUID

    model_config = ConfigDict(from_attributes=True)
