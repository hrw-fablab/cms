from email.policy import default
from wagtail.core import blocks


class GrabberBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    layout = blocks.ChoiceBlock(
        choices=[
            ("news-large", "Zeitungslayout mit einem Hauptelement"),
            ("news-medium", "Zeitungslayout mit zwei Hauptelementen"),
            ("extrem", "1 Element pro Reihe"),
            ("large", "2 Elemente pro Reihe"),
            ("medium", "3 Elemente pro Reihe"),
            ("small", "4 Elemente pro Reihe"),
        ],
        default="news-large",
        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
    )
    amount = blocks.IntegerBlock(default=5)
    pages = blocks.ListBlock(blocks.PageChooserBlock())

    class Meta:
        group = "Content Grabber"
        template = "templates/grabber.html"
        icon = "grip"
        abstract = True
