from uuid import UUID
from sqlalchemy.orm import Session
from app.models.table_column import TableColumn as TableColumnModel
from app.schemas.table_column import TableColumn as TableColumnSchema


class CRUDTableColumn:
    def create(
        self, db: Session, table_column_obj: TableColumnSchema
    ) -> TableColumnModel:
        table_column = TableColumnModel(
            name=table_column_obj.name,
            data_type=table_column_obj.data_type,
            database_table_id=table_column_obj.database_table_id,
        )
        db.add(table_column)
        db.flush()
        return table_column

    def get_by_database_table_id(
        self, db: Session, database_table_id: UUID
    ) -> TableColumnModel:
        return db.query(TableColumnModel).filter(
            TableColumnModel.database_table_id == database_table_id
        )
    
    def delete_by_database_table_id(self, db: Session, database_table_id: UUID) -> None:
        db.query(TableColumnModel).filter(
            TableColumnModel.database_table_id == database_table_id
        ).delete()
        db.commit()


crud_table_column = CRUDTableColumn()
