from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_current_user, get_db
from app.crud.crud_user_database import crud_user_database
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql import text
from app.services.query_service import query_service 
from app.constants import DQL
from app.utilities.fernet_manager import FernetManager
import logging

router = APIRouter()
logger = logging.getLogger("mql")

@router.get("/sql-data")
async def query_executor(
    db_id: str,
    sql_query: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    if not sql_query.lower().startswith(DQL["Statement_Type_Keyowrd"]):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Only DQL queries are allowed",
                "error": "Only DQL queries are allowed",
            },
        )
    try:
        database_connection_string = crud_user_database.get_by_id(db, db_id).connection_string
        password = current_user.hashed_key
        fernet_manager = FernetManager(password)
        database_connection_string = fernet_manager.decrypt(database_connection_string)
        if database_connection_string:
            engine = create_engine(database_connection_string)
            with engine.connect() as connection:
                result = connection.execute(text(sql_query))
                result = result.mappings().all()
                result_in_json_format = jsonable_encoder(result)
                result_in_2d_array = query_service.convert_to_2d_array(result_in_json_format)
                logger.info(
                    "Query {} executed successfully for user {} and database {}".format(
                        sql_query, current_user.id, db_id
                    )
                )

    except Exception as e:
        logger.error(
            "Error while executing query {} for user {} and database {}. Error is {}".format(
                sql_query, current_user.id, db_id, e
            )
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Query execution failed",
                "error": str(e),
            }
        )

    return JSONResponse(
        content={
            "message": "Query executed successfully",
            "data": {"sql_query": sql_query, "query_result": result_in_2d_array},
        },
        status_code=status.HTTP_200_OK,
    )
