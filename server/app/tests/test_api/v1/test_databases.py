from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.crud.crud_database_table import crud_database_table
from app.crud.crud_table_column import crud_table_column
from app.crud.crud_user_database import crud_user_database
from app.models.user import User as UserModel
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utilities.fernet_manager import FernetManager
from sqlalchemy import text,MetaData
from app.models.user_database import UserDatabase
from app.models.database_table import DatabaseTable
from app.models.table_column import TableColumn
import os


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
        with open("server/output_schema.txt", "rb") as file:
            response = client.post(
                "/api/v1/upload-database-schema",
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

    response = client.get("/api/v1/databases", headers=headers)

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["data"]["user_databases"] is not None
    assert len(response_content["data"]["user_databases"]) == 0




def test_get_databases_for_user_with_one_database(
    client: TestClient, valid_user_model: UserModel, valid_jwt: str
) -> None:
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

    response = client.get("/api/v1/databases", headers=headers)

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["data"]["user_databases"] is not None
    assert len(response_content["data"]["user_databases"]) == 1
    assert response_content["data"]["user_databases"][0]["name"] == "Test"
    assert response_content["data"]["user_databases"][0]["id"] is not None
    assert response_content["data"]["user_databases"][0]["user_id"] == str(valid_user_model.id)
    assert response_content["data"]["user_databases"][0]["created_at"] is not None
    assert response_content["data"]["user_databases"][0]["updated_at"] is not None



def test_connect_to_database(
    client: TestClient, db: Session, valid_user_model: UserModel, valid_jwt: str
) -> None:
    mock_user = valid_user_model

    headers = {"Authorization": f"Bearer {valid_jwt}"}
    test_data = {
        "database_name": "mql_test",
        "database_user": "shuru",
        "database_password": "password",
        "database_host": "localhost",
        "database_port": "5435",
    }
    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=mock_background_task,
    ):
         response = client.post(
                "/api/v1/connect-database",
                data=test_data,
                headers=headers,
            )
        
           

    assert response.status_code == 202

    user_database = crud_user_database.get_by_user_id(db=db, user_id=mock_user.id)[0]
    assert user_database.name == "mql_test"
    assert user_database is not None
    assert user_database.user_id == mock_user.id
    assert user_database.name is not None
    database_tables = crud_database_table.get_by_user_database_id(
        db=db, user_database_id=user_database.id
    )
    print(database_table.name for database_table in database_tables.all())
    assert database_tables.count() == 6
    assert set(
        [database_table.name for database_table in database_tables.all()]
    ) == set(
        [
            "users",
            "embeddings",
            "queries",
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
    
    assert table_columns.count() == 6
    assert set([table_column.name for table_column in table_columns.all()]) == set(
        ["id", "name", "email", "hashed_password","created_at","updated_at"]
    )
    assert set([table_column.data_type for table_column in table_columns.all()]) == set(
        ["UUID", "VARCHAR", "VARCHAR", "VARCHAR","TIMESTAMP","TIMESTAMP"]
    )
    assert set(
        [table_column.database_table_id for table_column in table_columns.all()]
    ) == set([database_tables.filter_by(name="users").first().id])

def test_sync_schema(
    client: TestClient, db: Session, valid_user_model: UserModel, valid_jwt: str,
) -> None:
    headers = {"Authorization": f"Bearer {valid_jwt}"}
    with patch(
        "app.services.embeddings_service.embeddings_service.create_embeddings",
        side_effect=mock_background_task,
    ):
        connection_string = os.getenv("TEST_DATABASE_URL")
        engine = create_engine(connection_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        fernet_manager = FernetManager(valid_user_model.hashed_key)
        user_database_obj = UserDatabase(name="mql_test", user_id=valid_user_model.id, connection_string=fernet_manager.encrypt(connection_string))

        user_database = crud_user_database.create(
            db=db, user_database_obj=user_database_obj
        )
        metadata = MetaData()
        metadata.reflect(engine)
        tables = metadata.tables
        
        for table_name in tables.keys():
            database_table_obj = DatabaseTable(
                    name=table_name, user_database_id=user_database.id
                )
            database_table = crud_database_table.create(
                    db=db, database_table_obj=database_table_obj
                )
            for column in tables[table_name].columns:
                column_type = str(column.type).split("(")[0]
                table_column_obj = TableColumn(
                    name=column.name,
                    data_type=column_type,
                    database_table_id=database_table.id,
                )
                crud_table_column.create(db=db, table_column_obj=table_column_obj)
        db.commit()
        user_database = crud_user_database.get_by_user_id(db=db, user_id=valid_user_model.id)[0]
        assert user_database is not None
        assert user_database.user_id == valid_user_model.id
        assert user_database.name == "mql_test"
        engine = create_engine(connection_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(text("CREATE TABLE new_table (id UUID PRIMARY KEY, name VARCHAR, email VARCHAR, created_at TIMESTAMP)"))
        session.commit()
        database_id = user_database.id
        response = client.post(
            "api/v1/schema-sync",
            headers=headers,
            data={"database_id":str(database_id)},  
        )
        assert response.status_code == 200
        database_tables = crud_database_table.get_by_user_database_id(
            db=db, user_database_id=user_database.id
        )
        assert database_tables.count() == 7
        assert set(
            [database_table.name for database_table in database_tables.all()]
        ) == set(
            [
                "users",
                "embeddings",
                "queries",
                "user_databases",
                "database_tables",
                "table_columns",
                "new_table"
            ]
        )
        assert set(
            [database_table.user_database_id for database_table in database_tables.all()]
        ) == set([user_database.id])
        table_columns = crud_table_column.get_by_database_table_id(
            db, database_tables.filter_by(name="new_table").first().id
        )
        assert table_columns.count() == 4
        assert set([table_column.name for table_column in table_columns.all()]) == set(
            ["id", "name", "email", "created_at"]
        )
        assert set([table_column.data_type for table_column in table_columns.all()]) == set(
            ["UUID", "VARCHAR", "VARCHAR", "TIMESTAMP"]
        )
        assert set(
            [table_column.database_table_id for table_column in table_columns.all()]
        ) == set([database_tables.filter_by(name="new_table").first().id])
        session.execute(text("DROP TABLE new_table"))
        session.query(UserDatabase).filter(UserDatabase.id == user_database.id).delete()
        session.query(DatabaseTable).filter(DatabaseTable.user_database_id == user_database.id).delete()
        session.query(TableColumn).filter(TableColumn.database_table_id == database_tables.filter_by(name="new_table").first().id).delete()
        session.commit()
        session.close()
        engine.dispose()

