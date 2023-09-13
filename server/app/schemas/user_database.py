from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class UserDatabase(BaseModel):
    name: str
    user_id: UUID
    connection_string: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
