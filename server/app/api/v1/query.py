from fastapi import APIRouter, Depends, status, Form, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_current_user, get_db
from app.clients.openai_client import openai_client
from app.services.openai_service import openai_service
from app.services.embeddings_service import embeddings_service
from app.crud.crud_query import crud_query
from app.schemas.query import Query as QuerySchema
from app.crud.crud_user_database import crud_user_database
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError,DBAPIError,StatementError,ProgrammingError
from app.services.query_service import query_service 
import json
from typing import Annotated
import logging

router = APIRouter()
logger = logging.getLogger("mql")


@router.post("/queries")
async def query(
    db_id: Annotated[str, Form()],
    nl_query: Annotated[str, Form()],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query_schema = QuerySchema(
            nl_query=nl_query, user_database_id=db_id
        )
        query_record = crud_query.create(db, query_schema)
        query_embedding = openai_client.get_embeddings([nl_query])[0]
        relevant_table_text_nodes = embeddings_service.get_relevant_tables_for_query(
            query_embedding, db_id, db
        )
        sql_query = openai_service.text_2_sql_query(nl_query, relevant_table_text_nodes)
        if sql_query[-1] != ";":
            sql_query += ";"
        crud_query.insert_sql_query_by_id(
            db, query_record.id, sql_query
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

@router.get("/queries")
async def get_queries(
    db_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query = crud_query.get_by_datatbase_id_where_sql_query_not_null(
            db, db_id
        )
    except Exception as e:
        logger.error(
            "Error while fetching query for user {} and database {}. Error is {}".format(
                current_user.id, db_id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return JSONResponse(
        content={
            "message": "Queries fetched successfully",
            "data": {
                "queries": [
                    query.as_dict() for query in query
                ],
            },
        },
        status_code=status.HTTP_200_OK,
    )


@router.get("/queries/{id}")
async def get_query(
    id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    try:
        query = crud_query.get_by_id(db, id)
    except Exception as e:
        logger.error(
            "Error while fetching query {} for user {}. Error is {}".format(
                id, current_user.id, e
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
    return JSONResponse(
        content={
            "message": "Query fetched successfully",
            "data": {"query": query.as_dict()},
        },
        status_code=status.HTTP_200_OK,
    )
