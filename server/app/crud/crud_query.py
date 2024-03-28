from uuid import UUID
from sqlalchemy.orm import Session
from app.models.query import Query as QueryModel
from app.schemas.query import Query as QuerySchema


class CRUDQuery:
    def create(
        self, db: Session, query_obj: QuerySchema
    ) -> QueryModel:
        query = QueryModel(
            nl_query=query_obj.nl_query,
            user_database_id=query_obj.user_database_id,
            sql_query=query_obj.sql_query,
        )
        db.add(query)
        db.commit()
        db.refresh(query)
        return query

    def get_by_id(self, db: Session, id: UUID) -> QueryModel:
        return db.query(QueryModel).filter(QueryModel.id == id).first()

    def get_by_database_id(
        self, db: Session, user_database_id: UUID
    ) -> QueryModel:
        return db.query(QueryModel).filter(
            QueryModel.user_database_id == user_database_id
        )

    def get_by_datatbase_id_where_sql_query_not_null(
        self, db: Session, user_database_id: UUID
    ) -> QueryModel:
        return (
            db.query(QueryModel)
            .filter(QueryModel.user_database_id == user_database_id)
            .filter(QueryModel.sql_query != None)
        )

    def insert_sql_query_by_id(
        self, db: Session, id: UUID, sql_query: str
    ) -> QueryModel:
        query = (
            db.query(QueryModel).filter(QueryModel.id == id).first()
        )
        if query.sql_query is not None:
            raise ValueError("SQL query already exists")
        query.sql_query = sql_query
        db.commit()
        return query


crud_query = CRUDQuery()
