from llm.client import generate

from models.topic import TopicOutput
from models.audience import AudienceOutput


class AudienceAgent:

    def run(self, topic: TopicOutput) -> AudienceOutput:

        system_prompt = """
        You are an audience strategist.

        Evaluate which audience would be most interested
        in the topic.

        Return:
        - audience
        - reason
        - score from 1 to 10
        """

        user_prompt = f"""
        Topic: {topic.topic}

        Angle: {topic.angle}

        Emotion: {topic.emotion}
        """

        return generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=AudienceOutput,
        )