from app.crud.crud_embedding import CRUDEmbedding
import pytest
import numpy
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.crud.crud_user_database import CRUDUserDatabase
from app.services.embeddings_service import EmbeddingsService
from app.clients.openai_client import OpenAIClient 


mock_openai_embedding_response = {
    "data": [
        [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [0.1], [0.11], [0.12], [0.13], [0.14], [0.15], [0.16], [0.17], [0.18],
    ]
}


def mock_embedding_create(*args, **kwargs) -> dict:
    return mock_openai_embedding_response


def mock_background_task(*args, **kwargs) -> None:
    return None


@pytest.fixture
def embeddings_service() -> EmbeddingsService:
    return EmbeddingsService()


def test_create_embeddings(
    client: TestClient,
    db: Session,
    valid_user_model: UserModel,
    valid_jwt: str,
    embeddings_service: EmbeddingsService,
) -> None:
    crud_user_database = CRUDUserDatabase()
    crud_embedding = CRUDEmbedding()
    headers = {"Authorization": f"Bearer {valid_jwt}"}

    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=mock_background_task,
    ):
        with open("server/output_schema.txt", "rb") as file:
            response = client.post(
                "/api/v1/upload-database-schema",
                files={"file": file},
                data={"database_name": "Test"},
                headers=headers,
            )

    assert response.status_code == 202

    user_database = crud_user_database.get_by_user_id(
        db=db, user_id=valid_user_model.id
    )[0]
    assert user_database is not None
    assert user_database.user_id == valid_user_model.id
    assert user_database.name == "Test"

    with patch.object(OpenAIClient, 'get_embeddings', return_value=mock_openai_embedding_response['data']) as mock_method:
        
        embeddings_service.create_embeddings(db=db, database_id=str(user_database.id))

    result = crud_embedding.get_by_user_database_id(
        db=db, user_database_id=user_database.id
    )

    assert result.count() == 6
    for index in range(0, 6):
        assert result[index].embeddings_vector is not None
        assert result[index].database_table_id is not None
        assert result[index].user_database_id == user_database.id
