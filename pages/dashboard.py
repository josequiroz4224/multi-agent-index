# pages/dashboard.py

from nicegui import ui


def create_dashboard():

    ui.label(
        "Multi-Agent Intelligence Platform"
    ).classes(
        "text-4xl font-bold"
    )

    ui.label(
        "AI-powered workflow orchestration platform"
    )

    ui.separator()

    with ui.card().classes("w-full"):
        ui.label(
            "🟢 Content Intelligence"
        ).classes(
            "text-xl font-bold"
        )

        ui.label(
            "Trend → Topic → Audience → Hook"
        )

        ui.button(
            "Open Workflow",
            on_click=lambda: ui.navigate.to("/content")
        )

    with ui.card().classes("w-full"):
        ui.label(
            "🟡 Supply Chain Intelligence"
        ).classes(
            "text-xl font-bold"
        )

        ui.label(
            "Coming Soon"
        )

    with ui.card().classes("w-full"):
        ui.label(
            "🟡 Manufacturing Intelligence"
        ).classes(
            "text-xl font-bold"
        )

        ui.label(
            "Coming Soon"
        )

    with ui.card().classes("w-full"):
        ui.label(
            "🟡 Investment Intelligence"
        ).classes(
            "text-xl font-bold"
        )

        ui.label(
            "Coming Soon"
        )