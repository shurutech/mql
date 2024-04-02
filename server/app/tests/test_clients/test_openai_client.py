import pytest
from unittest.mock import patch
from app.clients.openai_client import openai_client as OpenAIClient

mock_openai_embedding_response = {
    "data": [
        {"embedding": [0.1, 0.2, 0.3]},
        {"embedding": [0.4, 0.5, 0.6]},
    ]
}

mock_chat_response = {
    'id': 'chatcmpl-99TiMJDtVEyznHcIbhatdpz9mYbzV',
    'choices': [
        {
            'finish_reason': 'stop',
            'index': 0,
            'message': {
                'content': "\n\nHello there, I am fine.\nhow may I assist you today?",
                'role': 'system',
            }
        }
    ],
    'created': 1712046202,
    'model': 'gpt-4-0613',
    'object': 'chat.completion',
    'usage': {
        'completion_tokens': 64, 
        'prompt_tokens': 356, 
        'total_tokens': 420
    }
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

    with patch.object(OpenAIClient, 'get_embeddings', return_value=[
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    ]) as mock_method:
        embeddings = openai_client.get_embeddings(nodes)

    assert embeddings == [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]


def test_get_chat_response(openai_client):
    messages = [{"role": "system", "content": "Hello, How are you?"}]

    with patch.object(OpenAIClient, 'get_chat_response', return_value={'response': mock_chat_response}) as mock_method:
        chat_response = openai_client.get_chat_response(messages)
    
    expected_response = {'response': mock_chat_response}

    assert chat_response == expected_response, "The chat response did not match the expected output."
