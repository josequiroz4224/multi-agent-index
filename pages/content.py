from nicegui import ui


@ui.page("/content")
def content_page():

    ui.label(
        "Content Intelligence Workflow"
    ).classes(
        "text-3xl font-bold"
    )

    ui.button(
        "Back",
        on_click=lambda: ui.navigate.to("/")
    )