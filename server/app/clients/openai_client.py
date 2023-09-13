from fastapi import HTTPException
from typing import List
import openai
import os
import logging

openai.api_key = os.getenv("OPENAI_API_KEY")

logger = logging.getLogger("analytics")


class OpenAIClient:
    def get_embeddings(self, nodes: list) -> List[list]:
        return [
            v["embedding"]
            for v in openai.Embedding.create(
                input=nodes, model="text-embedding-ada-002"
            )["data"]
        ]

    def get_chat_response(
        self, messages: List[dict], model: str = "gpt-4", temperature: float = 0.5
    ) -> dict:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                messages=messages,
            )
        except openai.error.Timeout as e:
            logger.error(
                "Timeout while getting chat response from openai. Error is {}".format(e)
            )
            raise HTTPException(
                status_code=408,
                detail="Timeout while getting chat response from openai",
            )
        except openai.error.APIError as e:
            logger.error(
                "APIError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except openai.error.APIConnectionError as e:
            logger.error(
                "APIConnectionError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except openai.error.InvalidRequestError as e:
            logger.error(
                "InvalidRequestError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except openai.error.AuthenticationError as e:
            logger.error(
                "AuthenticationError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except openai.error.PermissionError as e:
            logger.error(
                "PermissionError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except openai.error.RateLimitError as e:
            logger.error(
                "RateLimitError while getting chat response from openai. Error is {}".format(
                    e
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )
        except Exception as e:
            logger.error(
                "Error while getting chat response from openai. Error is {}".format(e)
            )
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )

        return response


openai_client = OpenAIClient()
