from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.crud.crud_database_table import crud_database_table
from app.crud.crud_table_column import crud_table_column
from app.crud.crud_user_database import crud_user_database
from app.models.user import User as UserModel
from unittest.mock import patch


def mock_background_task(*args, **kwargs) -> None:
    return None


def test_upload_file_happy_path(
    client: TestClient, db: Session, valid_user_model: UserModel, valid_jwt: str
) -> None:
    mock_user = valid_user_model

    headers = {"Authorization": f"Bearer {valid_jwt}"}
    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=mock_background_task,
    ):
        with open("output_schema.txt", "rb") as file:
            response = client.post(
                "/v1/databases",
                files={"file": file},
                data={"database_name": "Test"},
                headers=headers,
            )

    assert response.status_code == 202

    user_database = crud_user_database.get_by_user_id(db=db, user_id=mock_user.id)[0]
    assert user_database.name == "Test"
    assert user_database is not None
    assert user_database.user_id == mock_user.id
    assert user_database.name is not None
    database_tables = crud_database_table.get_by_user_database_id(
        db=db, user_database_id=user_database.id
    )
    assert database_tables.count() == 6
    assert set(
        [database_table.name for database_table in database_tables.all()]
    ) == set(
        [
            "users",
            "embeddings",
            "alembic_version",
            "user_databases",
            "database_tables",
            "table_columns",
        ]
    )
    assert set(
        [database_table.user_database_id for database_table in database_tables.all()]
    ) == set([user_database.id])
    table_columns = crud_table_column.get_by_database_table_id(
        db, database_tables.filter_by(name="users").first().id
    )
    assert table_columns.count() == 4
    assert set([table_column.name for table_column in table_columns.all()]) == set(
        ["id", "name", "email", "hashed_password"]
    )
    assert set([table_column.data_type for table_column in table_columns.all()]) == set(
        ["uuid", "character varying", "character varying", "character varying"]
    )
    assert set(
        [table_column.database_table_id for table_column in table_columns.all()]
    ) == set([database_tables.filter_by(name="users").first().id])


def test_get_databases_for_user_with_zero_databases(
    client: TestClient, valid_jwt: str
) -> None:
    headers = {"Authorization": f"Bearer {valid_jwt}"}

    response = client.get("/v1/databases", headers=headers)

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["user_databases"] is not None
    assert len(response_content["user_databases"]) == 0


def test_get_databases_for_user_with_one_database(
    client: TestClient, valid_user_model: UserModel, valid_jwt: str
) -> None:
    headers = {"Authorization": f"Bearer {valid_jwt}"}

    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=mock_background_task,
    ):
        with open("output_schema.txt", "rb") as file:
            response = client.post(
                "/v1/databases",
                files={"file": file},
                data={"database_name": "Test"},
                headers=headers,
            )
    assert response.status_code == 202

    response = client.get("/v1/databases", headers=headers)

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["user_databases"] is not None
    assert len(response_content["user_databases"]) == 1
    assert response_content["user_databases"][0]["name"] == "Test"
    assert response_content["user_databases"][0]["id"] is not None
    assert response_content["user_databases"][0]["user_id"] == str(valid_user_model.id)
    assert response_content["user_databases"][0]["created_at"] is not None
    assert response_content["user_databases"][0]["updated_at"] is not None
