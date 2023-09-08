from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    id: Optional[UUID] = None

    model_config = ConfigDict(from_attributes=True)
