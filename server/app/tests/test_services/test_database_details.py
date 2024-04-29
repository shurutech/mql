import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.services.database_details import DatabaseDetails
from app.crud.crud_user_database import CRUDUserDatabase


def mock_background_task(*args, **kwargs) -> None:
    return None


@pytest.fixture
def database_details() -> DatabaseDetails:
    return DatabaseDetails()


def test_fetch_database_details(
    client: TestClient,
    db: Session,
    valid_user_model: UserModel,
    valid_jwt: str,
    database_details: DatabaseDetails,
) -> None:
    crud_user_database = CRUDUserDatabase()

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

    content = database_details.fetch_database_details(
        database_id=str(user_database.id), db=db
    )

    assert content["database_id"] == str(user_database.id)
    assert content["database_name"] == user_database.name
    assert len(content["database_tables"]) == 6
    assert set([table["table_name"] for table in content["database_tables"]]) == set(
        [
            "users",
            "embeddings",
            "alembic_version",
            "user_databases",
            "database_tables",
            "table_columns",
        ]
    )

    for table in content["database_tables"]:
        assert table["table_id"] is not None
        assert len(table["table_columns"]) > 0
        for column in table["table_columns"]:
            assert column["column_id"] is not None
            assert column["column_name"] is not None
            assert column["column_type"] is not None
