from llm.client import generate

from models.topic import TopicOutput
from models.audience import AudienceOutput
from models.hook import HookOutput


class HookAgent:

    def run(
        self,
        topic: TopicOutput,
        audience: AudienceOutput,
    ) -> HookOutput:

        system_prompt = """
        You are an expert content strategist.

        Create a compelling content hook.

        Return:
        - hook
        - explanation
        """

        user_prompt = f"""
        Topic:
        {topic.topic}

        Angle:
        {topic.angle}

        Audience:
        {audience.audience}

        Audience Reason:
        {audience.reason}

        Audience Score:
        {audience.score}
        """

        return generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=HookOutput,
        )