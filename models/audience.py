from pydantic import BaseModel


class AudienceOutput(BaseModel):
    audience: str
    reason: str
    score: int