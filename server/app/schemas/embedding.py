from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class Embedding(BaseModel):
    id: Optional[UUID] = None
    embeddings_vector: List[float]
    database_table_id: UUID
    user_database_id: UUID

    model_config = ConfigDict(from_attributes=True)
