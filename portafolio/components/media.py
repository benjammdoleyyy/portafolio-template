import reflex as rx

from portafolio.components.icon_button import icon_button

from portafolio.data import Media

from portafolio.styles.styles import Size





def media(data: Media) -> rx.Component:

    return rx.flex(

        icon_button(

            "mail",

            f"mailto:{data.email}?subject=Consulta%20sobre%20servicios&body=Hola,%20quisiera%20conocer%20más%20sobre%20tus%20servicios.",

            data.email,

            True

        ),

        rx.hstack(

            icon_button(

                "file-text",

                data.cv

            ),

            icon_button(

                "github",

                data.github

            ),

            icon_button(

                "linkedin",

                data.likedin

            ),

            spacing=Size.SMALL.value

        ),

        spacing=Size.SMALL.value,

        flex_direction=["column", "column", "row"]

    )

