from pydantic import BaseModel


class TopicOutput(BaseModel):
    topic: str
    angle: str
    emotion: str