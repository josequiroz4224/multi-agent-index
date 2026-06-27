from llm.client import generate
from models.trend import TrendOutput


class TrendAgent:

    def run(self) -> TrendOutput:

        system_prompt = """
        You are an expert technology trend analyst.

        Your job is to identify emerging AI trends that are valuable for ambitious
        Latino professionals, entrepreneurs, and content creators.

        Return only the three strongest trends.
        """

        user_prompt = """
        Find the top 3 AI trends that ambitious Latino professionals should understand this week.
        """

        return generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=TrendOutput,
        )