import pytest
from unittest.mock import patch
from app.services.openai_service import openai_service as OpenAIService
from app.clients.openai_client import OpenAIClient 
from unittest.mock import MagicMock

mock_choice = MagicMock()
mock_choice.message.content = "some_generated_sql_query;"
mock_chat_completion_object = MagicMock()
mock_chat_completion_object.choices = [mock_choice]



mock_openai_chat_response = {
    "id": "chatcmpl-7mdUAqgxJlviahl2xORk7wLSDmtN6",
    "object": "chat.completion",
    "created": 1691825882,
    "model": "gpt-4-0613",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "some_generated_sql_query;\nSQLResult: sample_sql_result\n\nAnswer: sample_answer.",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 75, "completion_tokens": 39, "total_tokens": 114},
}


def mock_chat_response(*args, **kwargs) -> dict:
    return mock_openai_chat_response


@pytest.fixture
def openai_service() -> OpenAIService:
    return OpenAIService


def test_text_2_sql_query(openai_service) -> None:
    query_str = "user_query"
    relevant_table_schema = "relevant_table_schema_from_db"
    dialect = "postgresql"

    with patch.object(OpenAIClient, 'get_chat_response', return_value={'response': mock_chat_completion_object}):

        sql_query = openai_service.text_2_sql_query(
            query_str, relevant_table_schema, dialect
        )

    assert sql_query == "some_generated_sql_query;"
