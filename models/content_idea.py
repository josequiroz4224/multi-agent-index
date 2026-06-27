from pydantic import BaseModel

from models.topic import TopicOutput
from models.audience import AudienceOutput
from models.hook import HookOutput


class ContentIdea(BaseModel):
    topic: TopicOutput
    audience: AudienceOutput
    hook: HookOutput