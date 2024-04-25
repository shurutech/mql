from sqlalchemy.orm import Session
from app.clients.openai_client import openai_client
from app.crud.crud_database_table import crud_database_table
from app.services.database_details import database_details
from app.crud.crud_embedding import crud_embedding
from app.schemas.embedding import Embedding as EmbeddingSchema


class EmbeddingsService:
    def __create_node_for_table(self, table_details: dict):
        template = (
            "Schema of table {table_name}:\n"
            "Table '{table_name}' has columns: {columns} "
        )
        columns = []
        for column in table_details["table_columns"]:
            columns.append(f"{column['column_name']} ({column['column_type']})")
        column_str = ", ".join(columns)
        text_node = template.format(
            table_name=table_details["table_name"], columns=column_str
        )
        return text_node

    def create_embeddings(self, database_id: str, db: Session):
        try:
            db_details = database_details.fetch_database_details(database_id, db)
            text_nodes_of_tables = dict()
            for table_details in db_details["database_tables"]:
                text_node = self.__create_node_for_table(table_details)
                crud_database_table.upsert_text_node_by_id(
                    db, table_details["table_id"], text_node
                )
                text_nodes_of_tables[table_details["table_id"]] = text_node

            table_embeddings = openai_client.get_embeddings(
                list(text_nodes_of_tables.values())
            )

            for idx, table_id in enumerate(text_nodes_of_tables.keys()):
                embedding_vector = table_embeddings[idx]
                
                crud_embedding.create(
                    db,
                    EmbeddingSchema(
                        embeddings_vector=embedding_vector,
                        database_table_id=table_id,
                        user_database_id=database_id,
                    ),
                )
        except Exception as e:
            print(e)
            raise e

    def get_relevant_tables_for_query(
        self, query_embedding: list[float], database_id: str, db: Session
    ):
        try:
            closest_database_table_ids = (
                crud_embedding.get_closest_embeddings_by_database_id(
                    query_embedding, database_id, db
                )
            )
            closest_database_tables = [
                database_table.text_node
                for database_table in crud_database_table.get_by_ids(
                    db, closest_database_table_ids
                )
            ]
            return closest_database_tables
        except Exception as e:
            print(e)
            raise e


embeddings_service = EmbeddingsService()
