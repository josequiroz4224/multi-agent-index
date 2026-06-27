from pydantic import BaseModel


class HookOutput(BaseModel):
    hook: str
    explanation: str