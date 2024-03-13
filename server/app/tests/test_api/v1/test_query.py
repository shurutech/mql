import uuid
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import patch
from app.models.user import User as UserModel
from app.crud.crud_user_database import crud_user_database
from app.crud.crud_query_history import crud_query_history
from app.schemas.user_database import UserDatabase as UserDatabaseSchema
from app.schemas.query_history import QueryHistory as QueryHistorySchema

mock_openai_embedding_response = {
    "data": [
        {"embedding": [0.1, 0.2, 0.3]},
        {"embedding": [0.4, 0.5, 0.6]},
    ]
}

mock_openai_chat_response = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "gpt-4",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "system",
                "content": "SELECT * FROM employee",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 9, "completion_tokens": 12, "total_tokens": 21},
}

mock_openai_chat_response_with_connection_db = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "gpt-4",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "shuru",
                "content": "SELECT count(*) FROM users",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 9, "completion_tokens": 12, "total_tokens": 21},
}

mock_database_connection_response = {
    "message": "Database connected successfully",
    "data": {
        "database_id": "15b18c1a-6939-4b82-9166-3e98e175f500",
        "database_name": "test"
    }
}


def mock_embedding_create(*args, **kwargs) -> dict:
    return mock_openai_embedding_response


def mock_chat_response(*args, **kwargs) -> dict:
    return mock_openai_chat_response

def mock_chat_response_with_connection_db(*args, **kwargs) -> dict:
    return mock_openai_chat_response_with_connection_db

def mock_database_connection(*args, **kwargs) -> dict:
    return mock_database_connection_response   


def test_query(
    client: TestClient, db: Session, valid_jwt: str, valid_user_model: UserModel
) -> None:
    headers = {"Authorization": f"Bearer {valid_jwt}"}

    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=None,
    ):
        with open("output_schema.txt", "rb") as file:
            response = client.post(
                "/v1/databases",
                files={"file": file},
                data={"database_name": "Test"},
                headers=headers,
            )

    assert response.status_code == 202
    database_id = crud_user_database.get_by_user_id(db=db, user_id=valid_user_model.id)[
        0
    ].id
    with (
        patch(
            "app.clients.openai_client.chat.completions.create",
            side_effect=mock_chat_response,
        ),
        patch(
            "app.clients.openai_client.openai.embeddings.create",
            side_effect=mock_embedding_create,
        ),
    ):
        response = client.post(
            f"/v1/query/{database_id}",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {valid_jwt}",
            },
            data={"nl_query": "show me the table schema of the table employee"},
        )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Query processed successfully",
        "data": {
            "sql_query": "SELECT * FROM employee",
            "nl_query": "show me the table schema of the table employee",
        },
    }


def test_query_history(
    client: TestClient, db: Session, valid_jwt: str, valid_user_model: UserModel
) -> None:
    database_obj = crud_user_database.create(
        db=db,
        user_database_obj=UserDatabaseSchema(
            name="Test",
            user_id=valid_user_model.id,
        ),
    )
    query_history_obj = crud_query_history.create(
        db=db,
        query_history_obj=QueryHistorySchema(
            nl_query="show me the table schema of the table employee",
            user_database_id=database_obj.id,
            sql_query="SELECT * FROM employee",
        ),
    )
    response = client.get(
        f"/v1/query/{database_obj.id}/history",
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Query histories fetched successfully",
        "data": {
            "query_histories": [
                {
                    "id": str(query_history_obj.id),
                    "nl_query": "show me the table schema of the table employee",
                    "sql_query": "SELECT * FROM employee",
                    "user_database_id": str(database_obj.id),
                    "created_at": query_history_obj.created_at.isoformat(),
                    "updated_at": query_history_obj.updated_at.isoformat(),
                }
            ],
        },
    }
        
        
   

def test_query_history_by_id(
    client: TestClient, db: Session, valid_jwt: str, valid_user_model: UserModel
) -> None:
    database_obj = crud_user_database.create(
        db=db,
        user_database_obj=UserDatabaseSchema(
            name="Test",
            user_id=valid_user_model.id,
        ),
    )
    query_history_obj = crud_query_history.create(
        db=db,
        query_history_obj=QueryHistorySchema(
            nl_query="show me the table schema of the table employee",
            user_database_id=database_obj.id,
            sql_query="SELECT * FROM employee",
        ),
    )
    response = client.get(
        f"/v1/query/{database_obj.id}/history/{query_history_obj.id}",
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Query history fetched successfully",
        "data":{
            "query_history": {
                "id": str(query_history_obj.id),
                "nl_query": "show me the table schema of the table employee",
                "sql_query": "SELECT * FROM employee",
                "user_database_id": str(database_obj.id),
                "created_at": query_history_obj.created_at.isoformat(),
                "updated_at": query_history_obj.updated_at.isoformat(),
        }
            
        }
    }

def test_query_for_connected_database(
    client: TestClient, db: Session, valid_jwt: str, valid_user_model: UserModel
) -> None:
    headers = {"Authorization": f"Bearer {valid_jwt}"}
    test_data = {
        "database_name": "analytics_test",
        "database_user": "shuru",
        "database_password": "password",
        "database_host": "localhost",
        "database_port": "5432",
    }

    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=None,
    ):
            response = client.post(
            "/v1/databases/connect",
            data=test_data,
            headers=headers,
        )
    assert response.status_code == 202
    database_id = crud_user_database.get_by_user_id(db=db, user_id=valid_user_model.id)[
        0
    ].id
    with (
        patch(
            "app.clients.openai_client.chat.completions.create",
            side_effect=mock_chat_response_with_connection_db,
        ),
        patch(
            "app.clients.openai_client.openai.embedding.create",
            side_effect=mock_embedding_create,
        ),
    ):
        response = client.post(
            f"/v1/query/{database_id}",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {valid_jwt}",
            },
            data={"nl_query": "show me the number of users in the table users","execute":True},
        )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Query processed successfully",
        "data": {
            
            "sql_query": "SELECT count(*) FROM users",
            "nl_query": "show me the number of users in the table users",
            'query_result': [{'count': 1}],
            
        }
    }

