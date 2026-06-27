from nicegui import ui

from agents.trend_agent import TrendAgent
from agents.topic_agent import TopicAgent
from agents.audience_agent import AudienceAgent
from agents.hook_agent import HookAgent


ui.query("body").style(
    "background-color: #f5f7fa;"
)

# Global UI references
status_label = None

trend_output_ui = None
topic_output_ui = None
audience_output_ui = None
hook_output_ui = None


def generate_content():

    global status_label
    global trend_output_ui
    global topic_output_ui
    global audience_output_ui
    global hook_output_ui

    status_label.set_text("Running Agents...")

    trend_agent = TrendAgent()
    topic_agent = TopicAgent()
    audience_agent = AudienceAgent()
    hook_agent = HookAgent()

    # Agent 1
    trend_output = trend_agent.run()
    selected_trend = trend_output.trends[0]

    # Agent 2
    topic = topic_agent.run(selected_trend)

    # Agent 3
    audience = audience_agent.run(topic)

    # Agent 4
    hook = hook_agent.run(topic, audience)

    trend_output_ui.content = f"""
## Trend

{selected_trend}
"""
    trend_output_ui.update()

    topic_output_ui.content = f"""
## Topic

**Topic:** {topic.topic}

**Angle:** {topic.angle}

**Emotion:** {topic.emotion}
"""
    topic_output_ui.update()

    audience_output_ui.content = f"""
## Audience

**Audience:** {audience.audience}

**Score:** {audience.score}/10

**Reason:** {audience.reason}
"""
    audience_output_ui.update()

    hook_output_ui.content = f"""
## Hook

{hook.hook}

### Why It Works

{hook.explanation}
"""
    hook_output_ui.update()

    status_label.set_text("Completed")



# ======================================================
# PAGE CONTAINER
# ======================================================

with ui.column().classes(
    "w-full max-w-7xl mx-auto p-8"
):
    
        
    # ======================================================
    # HEADER
    # ======================================================

    ui.label(
        "Multi-Agent Intelligence Platform"
    ).classes(
        "text-4xl font-bold"
    )

    ui.label(
        "AI Workflow Orchestration Engine"
    ).classes(
        "text-lg text-gray-500"
    )

    ui.label(
        "OpenAI • Structured Outputs • Pydantic • NiceGUI"
    ).classes(
        "text-sm text-gray-400"
    )

    # ======================================================
    # METRICS
    # ======================================================

    with ui.row().classes(
        "w-full justify-center gap-4 mb-4"
    ):

        with ui.card().classes(
            "w-56 text-center shadow-md"
        ):
            ui.label(
                "ACTIVE AGENTS"
            ).classes(
                "text-xs font-bold text-gray-500"
            )

            ui.label(
                "4"
            ).classes(
                "text-4xl font-bold"
            )

        with ui.card().classes(
            "w-56 text-center shadow-md"
        ):
            ui.label(
                "PYDANTIC MODELS"
            ).classes(
                "text-xs font-bold text-gray-500"
            )

            ui.label(
                "5"
            ).classes(
                "text-4xl font-bold"
            )

        with ui.card().classes(
            "w-56 text-center shadow-md"
        ):
            ui.label(
                "ACTIVE WORKFLOWS"
            ).classes(
                "text-xs font-bold text-gray-500"
            )

            ui.label(
                "1"
            ).classes(
                "text-4xl font-bold"
            )

        with ui.card().classes(
            "w-56 text-center shadow-md"
        ):
            ui.label(
                "LLM PROVIDER"
            ).classes(
                "text-xs font-bold text-gray-500"
            )

            ui.label(
                "OPENAI"
            ).classes(
                "text-2xl font-bold"
            )
    ui.separator()

    # ======================================================
    # TABS
    # ======================================================

    with ui.tabs().classes("w-full") as tabs:
        content_tab = ui.tab("Content Intelligence")
        supply_tab = ui.tab("Supply Chain Intelligence")
        manufacturing_tab = ui.tab("Manufacturing Intelligence")
        investment_tab = ui.tab("Investment Intelligence")

    with ui.tab_panels(tabs, value=content_tab).classes("w-full"):

        # ==================================================
        # CONTENT TAB
        # ==================================================

        with ui.tab_panel(content_tab):

            ui.label(
                "Content Intelligence"
            ).classes(
                "text-2xl font-bold"
            )

            ui.label(
                "Generate content ideas using a multi-agent workflow."
            )

            with ui.card().classes(
                "w-full shadow-sm"
            ):

                ui.label(
                    "CONTENT INTELLIGENCE WORKFLOW"
                ).classes(
                    "text-xs font-bold text-gray-500"
                )

                ui.separator()

                ui.label(
                    "Trend Agent → Topic Agent → Audience Agent → Hook Agent"
                ).classes(
                    "text-lg font-medium"
                )

            with ui.row().classes(
                "items-center gap-2"
            ):

                ui.icon(
                    "check_circle"
                ).classes(
                    "text-green-600"
                )

                status_label = ui.label(
                    "Ready"
                ).classes(
                    "text-green-600 font-bold"
                )

            ui.button(
                    "Generate Content Intelligence",
                    on_click=generate_content
                ).props(
                    "unelevated"
                ).classes(
                    "mb-4"
                )

            ui.separator()

            with ui.row().classes(
                "w-full gap-4"
            ):

                with ui.card().classes(
                    "col-grow shadow-md"
                ).style(
                    "width:48%; min-height:250px;"
                ):
                    trend_output_ui = ui.markdown("## Trend")

                with ui.card().classes(
                    "col-grow shadow-md"
                ).style(
                    "width:48%; min-height:250px;"
                ):
                    topic_output_ui = ui.markdown("## Topic")

            with ui.row().classes(
                "w-full gap-4"
            ):

                with ui.card().classes(
                    "col-grow shadow-md"
                ).style(
                    "width:48%; min-height:250px;"
                ):
                    audience_output_ui = ui.markdown("## Audience")

                with ui.card().classes(
                    "col-grow shadow-md"
                ).style(
                    "width:48%; min-height:250px;"
                ):
                    hook_output_ui = ui.markdown("## Hook")

        # ==================================================
        # SUPPLY CHAIN TAB
        # ==================================================

        with ui.tab_panel(supply_tab):

            ui.label(
                "Supply Chain Intelligence"
            ).classes(
                "text-2xl font-bold"
            )

            ui.label("🚧 Coming Soon")

            ui.markdown("""
    ### Planned Agents

    - Demand Agent
    - Inventory Agent
    - Risk Agent
    - Recommendation Agent

    Future Workflow:

    Demand → Inventory → Risk → Recommendation
    """)

        # ==================================================
        # MANUFACTURING TAB
        # ==================================================

        with ui.tab_panel(manufacturing_tab):

            ui.label(
                "Manufacturing Intelligence"
            ).classes(
                "text-2xl font-bold"
            )

            ui.label("🚧 Coming Soon")

            ui.markdown("""
    ### Planned Agents

    - KPI Agent
    - Bottleneck Agent
    - Root Cause Agent
    - Action Agent

    Future Workflow:

    KPI → Bottleneck → Root Cause → Action
    """)

        # ==================================================
        # INVESTMENT TAB
        # ==================================================

        with ui.tab_panel(investment_tab):

            ui.label(
                "Investment Intelligence"
            ).classes(
                "text-2xl font-bold"
            )

            ui.label("🚧 Coming Soon")

            ui.markdown("""
    ### Planned Agents

    - Market Agent
    - Sector Agent
    - Risk Agent
    - Opportunity Agent

    Future Workflow:

    Market → Sector → Risk → Opportunity
    """)

ui.run(
    title="Multi-Agent Intelligence Platform"
)