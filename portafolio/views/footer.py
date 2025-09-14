import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_button(
                "message-circle",
                f"https://wa.me/5356933884",
                "",
                False
            ),
            spacing=Size.SMALL.value,
            justify="center"
        ),
        rx.text(
            "© 2025 Neisser.tech - Todos los derechos reservados",
            text_align="center",
            font_size="sm",
            color="gray",
            margin_top=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        align="center",
        width="100%"
    )
