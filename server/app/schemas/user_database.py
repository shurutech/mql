from pydantic import BaseModel, ConfigDict
from uuid import UUID


class UserDatabase(BaseModel):
    name: str
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)
