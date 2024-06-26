from fastapi import (
    APIRouter,
    BackgroundTasks,
    status,
    HTTPException,
    Depends,
    UploadFile,
    File,
    Form,
)
from typing import Annotated
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData
from app.api.v1.dependencies import get_current_user, get_db
from app.crud.crud_database_table import crud_database_table
from app.crud.crud_table_column import crud_table_column
from app.crud.crud_user_database import crud_user_database
from app.schemas.database_table import DatabaseTable
from app.schemas.table_column import TableColumn
from app.schemas.user_database import UserDatabase
from app.services.embeddings_service import embeddings_service
from app.services.database_details import database_details
from app.utilities.fernet_manager import FernetManager
import logging

router = APIRouter()

logger = logging.getLogger("mql")

"""
TODO:Put a file structure validation here
"""

@router.post("/connect-database")
async def connect_to_database(
    database_name: Annotated[str, Form()],
    database_user: Annotated[str, Form()],
    database_password: Annotated[str, Form()],
    database_host: Annotated[str, Form()],
    database_port: Annotated[str, Form()],
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        connection_string = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"

        engine = create_engine(connection_string)
        try:
            engine.connect()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to connect to the database: " + str(e),
            )
        

        
        fernet_manager = FernetManager(current_user.hashed_key)
        logger.error("after fernet: %s" , connection_string)
        encrypted_connection_string = fernet_manager.encrypt(connection_string)

        user_database_obj = UserDatabase(name=f"{database_name}", user_id=current_user.id, connection_string=encrypted_connection_string)

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
        background_tasks.add_task(
            embeddings_service.create_embeddings, user_database.id, db

        )
 
    except Exception as e:
        db.rollback()
        logger.error(
            "Error occurred while connecting to database for user_id {}. Error is {}".format(
                current_user.id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Database connected successfully",
            "data": {"database_id": str(user_database.id), "database_name": user_database.name},
        },
        status_code=status.HTTP_202_ACCEPTED,
    )

@router.post("/upload-database-schema")
async def upload_file(
    background_tasks: BackgroundTasks,
    database_name: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        contents = await file.read()
        lines = contents.decode().split("\n")
        database_name = database_name or file.filename
        user_database_obj = UserDatabase(name=database_name, user_id=current_user.id)
        user_database = crud_user_database.create(
            db=db, user_database_obj=user_database_obj
        )

        table_name = None
        database_table = None
        for line in lines:
            if line.startswith("Table: "):
                table_name = line.split(": ")[1]

                database_table_obj = DatabaseTable(
                    name=table_name, user_database_id=user_database.id
                )
                database_table = crud_database_table.create(
                    db=db, database_table_obj=database_table_obj
                )
            elif line.strip() == "":
                table_name = None
                database_table = None
            elif table_name is not None and database_table is not None:
                column_name, data_type = map(str.strip, line.split("|"))

                table_column_obj = TableColumn(
                    name=column_name,
                    data_type=data_type,
                    database_table_id=database_table.id,
                )
                crud_table_column.create(db=db, table_column_obj=table_column_obj)
        db.commit()
        
        background_tasks.add_task(
            embeddings_service.create_embeddings, user_database.id, db
        )
    except Exception as e:
        db.rollback()
        logger.error(
            "Error occurred while uploading file for user_id {}. Error is {}".format(
                current_user.id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={"message": "File uploaded successfully", "data": None},
        status_code=status.HTTP_202_ACCEPTED,
    )


@router.get("/databases")
async def get_databases(
    db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    try:
        databases = crud_user_database.get_by_user_id(db, current_user.id)

    except Exception as e:
        logger.error(
            "Error occurred while fetching databases for user_id {}. Error is {}".format(
                current_user.id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Databases fetched successfully",
            "data": {
                "user_databases": [
                    user_database.as_dict() for user_database in databases
                ]
            },
        },
        status_code=status.HTTP_200_OK,
    )


"""
TODO: Create an index in db for user_id and database_id for validation
"""


@router.get("/databases/{database_id}")
async def get_single_database_details(
    database_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        databases = crud_user_database.get_by_user_id(db, current_user.id)
        databases_ids = [str(database.id) for database in databases]
        if database_id not in databases_ids:
            logger.info(
                "Database with database_id {} not found for user_id {}".format(
                    database_id, current_user.id
                )
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Database not found"
            )
        database_detail = database_details.fetch_database_details(database_id, db)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error(
            "Error occurred while fetching database details for database_id {}. Error is {}".format(
                database_id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
    return JSONResponse(
        content={"message": "Database details", "data": database_detail},
        status_code=status.HTTP_200_OK,
    )

@router.post("/schema-sync")
async def sync_database_schema(
    background_tasks: BackgroundTasks,
    database_id: Annotated[str, Form(...)],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        database = crud_user_database.get_by_id(db, database_id)
        logger.error("databases: %s", database)
        if database is None:
            logger.info(
                "Database with database_id {} not found for user_id {}".format(
                    database_id, current_user.id
                )
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Database not found"
            )
        database_tables = crud_database_table.get_by_user_database_id(db, database_id)
        for table in database_tables:
            crud_table_column.delete_by_database_table_id(db, table.id)
        crud_database_table.delete_by_user_database_id(db, database_id)
        metadata = MetaData()
        fernet_manager = FernetManager(current_user.hashed_key)
        user_database = crud_user_database.get_by_id(db, database_id)
        decrypted_connection_string = fernet_manager.decrypt(user_database.connection_string)
        logger.error("decrypted_connection_string: %s", decrypted_connection_string)
        engine = create_engine(decrypted_connection_string)
        metadata.reflect(engine)
        tables = metadata.tables
        for table_name in tables.keys():
            database_table_obj = DatabaseTable(
                name=table_name, user_database_id=database_id
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
        background_tasks.add_task(embeddings_service.create_embeddings, database_id, db)
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        logger.error(
            "Error occurred while refreshing database schema for database_id {}. Error is {}".format(
                database_id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
    return JSONResponse(
        content={"message": "Database schema refreshed successfully", "data": None},
        status_code=status.HTTP_200_OK,
    )
