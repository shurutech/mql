from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.database_table import DatabaseTable as DatabaseTableModel
from app.schemas.database_table import DatabaseTable as DatabaseTableSchema


class CRUDDatabaseTable:
    def create(
        self, db: Session, database_table_obj: DatabaseTableSchema
    ) -> DatabaseTableModel:
        database_table = DatabaseTableModel(
            name=database_table_obj.name,
            text_node=database_table_obj.text_node,
            user_database_id=database_table_obj.user_database_id,
        )
        db.add(database_table)
        db.flush()
        return database_table

    def get_by_user_database_id(
        self, db: Session, user_database_id: UUID
    ) -> DatabaseTableModel:
        return db.query(DatabaseTableModel).filter(
            DatabaseTableModel.user_database_id == user_database_id
        )

    def get_by_id(self, db: Session, id: UUID) -> DatabaseTableModel:
        return db.query(DatabaseTableModel).filter(DatabaseTableModel.id == id).first()

    def get_by_ids(
        self, db: Session, table_ids: List[UUID]
    ) -> List[DatabaseTableModel]:
        return db.query(DatabaseTableModel).filter(DatabaseTableModel.id.in_(table_ids))

    def upsert_text_node_by_id(
        self, db: Session, table_id: UUID, text_node: str
    ) -> None:
        database_table = (
            db.query(DatabaseTableModel)
            .filter(DatabaseTableModel.id == table_id)
            .first()
        )
        database_table.text_node = text_node
        db.commit()

    def delete_by_user_database_id(self, db: Session, user_database_id: UUID) -> None:
        db.query(DatabaseTableModel).filter(DatabaseTableModel.user_database_id == user_database_id).delete()

crud_database_table = CRUDDatabaseTable()
