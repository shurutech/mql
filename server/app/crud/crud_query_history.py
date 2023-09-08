from uuid import UUID
from sqlalchemy.orm import Session
from app.models.query_history import QueryHistory as QueryHistoryModel
from app.schemas.query_history import QueryHistory as QueryHistorySchema


class CRUDQueryHistory:
    def create(
        self, db: Session, query_history_obj: QueryHistorySchema
    ) -> QueryHistoryModel:
        query_history = QueryHistoryModel(
            nl_query=query_history_obj.nl_query,
            user_database_id=query_history_obj.user_database_id,
            sql_query=query_history_obj.sql_query,
        )
        db.add(query_history)
        db.commit()
        db.refresh(query_history)
        return query_history

    def get_by_id(self, db: Session, id: UUID) -> QueryHistoryModel:
        return db.query(QueryHistoryModel).filter(QueryHistoryModel.id == id).first()

    def get_by_database_id(
        self, db: Session, user_database_id: UUID
    ) -> QueryHistoryModel:
        return db.query(QueryHistoryModel).filter(
            QueryHistoryModel.user_database_id == user_database_id
        )

    def get_by_datatbase_id_where_sql_query_not_null(
        self, db: Session, user_database_id: UUID
    ) -> QueryHistoryModel:
        return (
            db.query(QueryHistoryModel)
            .filter(QueryHistoryModel.user_database_id == user_database_id)
            .filter(QueryHistoryModel.sql_query != None)
        )

    def insert_sql_query_by_id(
        self, db: Session, id: UUID, sql_query: str
    ) -> QueryHistoryModel:
        query_history = (
            db.query(QueryHistoryModel).filter(QueryHistoryModel.id == id).first()
        )
        if query_history.sql_query is not None:
            raise ValueError("SQL query already exists")
        query_history.sql_query = sql_query
        db.commit()
        return query_history


crud_query_history = CRUDQueryHistory()
