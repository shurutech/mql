import pytest
from unittest.mock import patch
from app.clients.openai_client import openai_client as OpenAIClient

mock_openai_embedding_response = {
    "data": [
        {"embedding": [0.1, 0.2, 0.3]},
        {"embedding": [0.4, 0.5, 0.6]},
    ]
}

mock_openai_chat_response = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "gpt-4",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "system",
                "content": "\n\nHello there, I am fine.\nhow may I assist you today?",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 9, "completion_tokens": 12, "total_tokens": 21},
}


def mock_embedding_create(*args, **kwargs) -> dict:
    return mock_openai_embedding_response


def mock_chat_response(*args, **kwargs) -> dict:
    return mock_openai_chat_response


@pytest.fixture
def openai_client() -> OpenAIClient:
    return OpenAIClient


def test_get_embeddings(openai_client) -> None:
    nodes = ["Hello", "World"]

    with patch(
        "app.clients.openai_client.openai.embeddings.create",
        side_effect=mock_embedding_create,
    ):
        embeddings = openai_client.get_embeddings(nodes)

    assert embeddings == [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]


def test_get_chat_response(openai_client) -> None:
    messages = [
        {
            "role": "system",
            "content": "Hello, How are you?",
        },
    ]

    with patch(
        "app.clients.openai_client.openai.ChatCompletion.create",
        side_effect=mock_chat_response,
    ):
        chat_response = openai_client.get_chat_response(messages)

    assert chat_response == {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gpt-4",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "system",
                    "content": "\n\nHello there, I am fine.\nhow may I assist you today?",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 9, "completion_tokens": 12, "total_tokens": 21},
    }
