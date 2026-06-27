from agents.trend_agent import TrendAgent
from agents.topic_agent import TopicAgent
from agents.audience_agent import AudienceAgent
from agents.hook_agent import HookAgent

from models.content_idea import ContentIdea


def main():

    # Initialize agents
    trend_agent = TrendAgent()
    topic_agent = TopicAgent()
    audience_agent = AudienceAgent()
    hook_agent = HookAgent()

    print("\n" + "=" * 60)
    print("MULTI-AGENT CONTENT INTELLIGENCE WORKFLOW")
    print("=" * 60)

    # Agent 1: Trend Agent
    trend_output = trend_agent.run()

    print("\nTREND OUTPUT")
    print("-" * 60)

    for i, trend in enumerate(trend_output.trends, start=1):
        print(f"{i}. {trend}")

    # Select first trend
    selected_trend = trend_output.trends[0]

    print("\nSELECTED TREND")
    print("-" * 60)
    print(selected_trend)

    # Agent 2: Topic Agent
    topic = topic_agent.run(selected_trend)

    print("\nTOPIC OUTPUT")
    print("-" * 60)
    print(f"Topic: {topic.topic}")
    print(f"Angle: {topic.angle}")
    print(f"Emotion: {topic.emotion}")

    # Agent 3: Audience Agent
    audience = audience_agent.run(topic)

    print("\nAUDIENCE OUTPUT")
    print("-" * 60)
    print(f"Audience: {audience.audience}")
    print(f"Reason: {audience.reason}")
    print(f"Score: {audience.score}/10")

    # Agent 4: Hook Agent
    hook = hook_agent.run(
        topic,
        audience,
    )

    print("\nHOOK OUTPUT")
    print("-" * 60)
    print(f"Hook: {hook.hook}")
    print(f"Explanation: {hook.explanation}")

    # Aggregate everything into one application object
    idea = ContentIdea(
        topic=topic,
        audience=audience,
        hook=hook,
    )

    print("\nCONTENT IDEA OBJECT")
    print("-" * 60)
    print(type(idea))

    print("\n" + "=" * 60)
    print("FINAL CONTENT IDEA")
    print("=" * 60)

    print(f"\nTOPIC:")
    print(idea.topic.topic)

    print(f"\nANGLE:")
    print(idea.topic.angle)

    print(f"\nAUDIENCE:")
    print(idea.audience.audience)

    print(f"\nAUDIENCE SCORE:")
    print(f"{idea.audience.score}/10")

    print(f"\nHOOK:")
    print(idea.hook.hook)

    print(f"\nWHY IT WORKS:")
    print(idea.hook.explanation)

    print("\n" + "=" * 60)
    print("WORKFLOW COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()