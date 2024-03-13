from app.clients.openai_client import openai_client


class OpenAIService:
    def __init__(self, DEFAULT_TEXT_TO_SQL_TMPL: str | None = None) -> None:
        self.__DEFAULT_TEXT_TO_SQL_TMPL = (
            "Given an input question, first create a syntactically correct {dialect} "
            "query to run, then look at the results of the query and return the answer. "
            "You can order the results by a relevant column to return the most "
            "interesting examples in the database.\n"
            "Never query for all the columns from a specific table, only ask for a "
            "few relevant columns given the question.\n"
            "Pay attention to use only the column names that you can see in the schema "
            "description. "
            "Be careful to not query for columns that do not exist. "
            "Pay attention to which column is in which table. "
            "Also, qualify column names with the table name when needed.\n"
            "Use the following format:\n"
            "Question: Question here\n"
            "SQLQuery: SQL Query to run\n"
            "SQLResult: Result of the SQLQuery\n"
            "Answer: Final answer here\n"
            "Only use the tables listed below.\n"
            "{schema}\n"
            "Question: {query_str}\n"
            "SQLQuery: "
        )

    def text_2_sql_query(
        self, query_str: str, relevant_table_schema: str, dialect: str = "postgresql"
    ) -> str:
        formatted_text_2_sql_prompt = self.__DEFAULT_TEXT_TO_SQL_TMPL.format(
            query_str=query_str, schema=relevant_table_schema, dialect=dialect
        )
        openai_response = openai_client.get_chat_response(
            messages=[
                {"role": "system", "content": formatted_text_2_sql_prompt},
            ],
        )
        chat_completion_object = openai_response['response']
        response = chat_completion_object.choices[0].message.content

        text2sql_response_copy = response
        sql_result_start = text2sql_response_copy.find("SQLResult:")
        if sql_result_start != -1:
            text2sql_response_copy = text2sql_response_copy[:sql_result_start]
        sql_query = text2sql_response_copy.strip()
        return sql_query


openai_service = OpenAIService()
