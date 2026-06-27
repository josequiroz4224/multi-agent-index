from llm.client import generate
from models.topic import TopicOutput


class TopicAgent:

    def run(self, trend: str) -> TopicOutput:

        system_prompt = """
        You are an expert content strategist.

        Your job is to transform trends into
        content opportunities.

        Return:
        - topic
        - angle
        - emotion
        """

        user_prompt = f"""
        Trend:

        {trend}

        Create a content topic.
        """

        return generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=TopicOutput,
        )