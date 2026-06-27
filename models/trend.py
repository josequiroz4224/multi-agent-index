from pydantic import BaseModel

class TrendOutput(BaseModel):
    trends: list[str]