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
from typing import Annotated
import logging

router = APIRouter()
logger = logging.getLogger("analytics")


@router.post("/query/{database_id}")
async def query(
    database_id: str,
    nl_query: Annotated[str, Form()],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_history_schema = QueryHistorySchema(
            nl_query=nl_query, user_database_id=database_id
        )
        query_history_record = crud_query_history.create(db, query_history_schema)
        query_embedding = openai_client.get_embeddings([nl_query])[0]
        relevant_table_text_nodes = embeddings_service.get_relevant_tables_for_query(
            query_embedding, database_id, db
        )
        sql_query = openai_service.text_2_sql_query(nl_query, relevant_table_text_nodes)
        crud_query_history.insert_sql_query_by_id(
            db, query_history_record.id, sql_query
        )

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error(
            "Error while processing query {} for user {} and database {}. Error is {}".format(
                nl_query, current_user.id, database_id, e
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


@router.get("/query/{database_id}/history")
async def get_query_history(
    database_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        database_name = crud_user_database.get_by_id(db, database_id).name
        query_history = crud_query_history.get_by_datatbase_id_where_sql_query_not_null(
            db, database_id
        )
    except Exception as e:
        logger.error(
            "Error while fetching query history for user {} and database {}. Error is {}".format(
                current_user.id, database_id, e
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


@router.get("/query/{database_id}/history/{query_history_id}")
async def get_query_history_by_id(
    database_id: str,
    query_history_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_history = crud_query_history.get_by_id(db, query_history_id)
    except Exception as e:
        logger.error(
            "Error while fetching query history {} for user {} and database {}. Error is {}".format(
                query_history_id, current_user.id, database_id, e
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
