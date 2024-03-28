from fastapi import APIRouter, Depends, status, Form, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_current_user, get_db
from app.clients.openai_client import openai_client
from app.services.openai_service import openai_service
from app.services.embeddings_service import embeddings_service
from app.crud.crud_query_history import crud_query_history
from app.schemas.query_history import QueryHistory as QueryHistorySchema
from app.crud.crud_user_database import crud_user_database
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql import text
import json
from typing import Annotated
import logging

router = APIRouter()
logger = logging.getLogger("analytics")


@router.post("/query")
async def query(
    db_id: Annotated[str, Form()],
    nl_query: Annotated[str, Form()],
    execute: Annotated[bool, Form()] = False,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_history_schema = QueryHistorySchema(
            nl_query=nl_query, user_database_id=db_id
        )
        query_history_record = crud_query_history.create(db, query_history_schema)
        query_embedding = openai_client.get_embeddings([nl_query])[0]
        relevant_table_text_nodes = embeddings_service.get_relevant_tables_for_query(
            query_embedding, db_id, db
        )
        sql_query = openai_service.text_2_sql_query(nl_query, relevant_table_text_nodes)
        crud_query_history.insert_sql_query_by_id(
            db, query_history_record.id, sql_query
        )
        if execute:
            database_connection_string = crud_user_database.get_by_id(db, db_id).connection_string
            if database_connection_string:
                engine = create_engine(database_connection_string)
                with engine.connect() as connection:
                    result = connection.execute(text(sql_query))
                    result = result.mappings().all()
                    result_in_json_format = jsonable_encoder(result)
                    logger.info(
                        "Query {} executed successfully for user {} and database {}".format(
                            sql_query, current_user.id, db_id
                        )
                    )
                    return JSONResponse(
                        content={
                            "message": "Query processed successfully",
                            "data": {"sql_query": sql_query, "nl_query": nl_query, "query_result": result_in_json_format},
                        },
                        status_code=status.HTTP_200_OK,
                    )
            
            
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error(
            "Error while processing query {} for user {} and database {}. Error is {}".format(
                nl_query, current_user.id, db_id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Query processed successfully",
            "data": {"sql_query": sql_query, "nl_query": nl_query},
        },
        status_code=status.HTTP_200_OK,
    )


@router.get("/query-history")
async def get_query_history(
    db_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_history = crud_query_history.get_by_datatbase_id_where_sql_query_not_null(
            db, db_id
        )
    except Exception as e:
        logger.error(
            "Error while fetching query history for user {} and database {}. Error is {}".format(
                current_user.id, db_id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Query histories fetched successfully",
            "data": {
                "query_histories": [
                    query_history.as_dict() for query_history in query_history
                ],
            },
        },
        status_code=status.HTTP_200_OK,
    )


@router.get("/query-history/{id}")
async def get_query_history_by_id(
    id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_history = crud_query_history.get_by_id(db, id)
    except Exception as e:
        logger.error(
            "Error while fetching query history {} for user {}. Error is {}".format(
                id, current_user.id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
    return JSONResponse(
        content={
            "message": "Query history fetched successfully",
            "data": {"query_history": query_history.as_dict()},
        },
        status_code=status.HTTP_200_OK,
    )
