from llm.client import client
from models.trend import TrendOutput

response = client.responses.parse(
    model="gpt-5.5",
    input=[
        {
            "role": "system",
            "content": "You are an expert technology trend analyst."
        },
        {
            "role": "user",
            "content": "Return the top 3 AI trends for ambitious Latino professionals."
        }
    ],
    text_format=TrendOutput,
)

trend = response.output_parsed

print(type(trend))
print(trend)
print(trend.trends)