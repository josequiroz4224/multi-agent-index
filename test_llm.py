from llm.client import generate

response = generate(
    system_prompt="You are a helpful assistant.",
    user_prompt="Tell me one interesting fact about AI agents."
)

print(response)