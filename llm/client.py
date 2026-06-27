import os

from typing import Type, TypeVar

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate(
    system_prompt: str,
    user_prompt: str,
    response_model: Type[T],
    model: str = "gpt-5.5",
) -> T:

    response = client.responses.parse(
        model=model,
        input=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        text_format=response_model,
    )
    # print("Response type:", type(response))
    # print("Parsed type:", type(response.output_parsed))
    # print("Parsed value:", response.output_parsed)

    return response.output_parsed