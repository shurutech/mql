from sqlalchemy.orm import Session
from app.crud.crud_database_table import crud_database_table
from app.crud.crud_table_column import crud_table_column
from app.crud.crud_user_database import crud_user_database


class DatabaseDetails:
    def fetch_database_details(self, database_id: str, db: Session):
        database_name = crud_user_database.get_by_id(db, database_id).name
        content = {
            "database_id": database_id,
            "database_name": database_name,
            "database_tables": [],
        }
        tables = crud_database_table.get_by_user_database_id(db, database_id)
        for table in tables:
            content["database_tables"].append(
                {
                    "table_id": str(table.id),
                    "table_name": table.name,
                    "table_columns": [],
                }
            )
            columns = crud_table_column.get_by_database_table_id(db, table.id)
            for column in columns:
                content["database_tables"][-1]["table_columns"].append(
                    {
                        "column_id": str(column.id),
                        "column_name": column.name,
                        "column_type": column.data_type,
                    }
                )
        return content


database_details = DatabaseDetails()
