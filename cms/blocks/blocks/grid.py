from wagtail import blocks

from .card import CardBlock
from .person import PersonBlock


class GridBlockElements(blocks.StreamBlock):
    card = CardBlock(label="Karte")
    person = PersonBlock(label="Person")


class GridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    layout = blocks.ChoiceBlock(
        choices=[
            ("extrem", "1 x N"),
            ("large", "2 x N"),
            ("medium", "3 x N"),
            ("small", "4 x N"),
        ],
        default="medium",
        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
    )
    style = blocks.ChoiceBlock(
        choices=[
            ("default", "Default"),
            ("variation", "Variation"),
        ],
        default="default",
    )

    cards = GridBlockElements(label="Grid Elemente")

    class Meta:
        group = "Cointainer"
        template = "blocks/grid.html"
        icon = "grip"
