from email.policy import default
from wagtail.core import blocks


class GrabberBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    layout = blocks.ChoiceBlock(
        choices=[
            ("newspaper", "Zeitungslayout mit einem Hauptelement"),
            ("magazine", "Zeitungslayout mit zwei Hauptelementen"),
            ("line", "3 Element pro Reihe"),
        ],
        default="newspaper",
        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
    )
    amount = blocks.IntegerBlock(default=5)
    pages = blocks.ListBlock(blocks.PageChooserBlock())

    class Meta:
        group = "Content Grabber"
        template = "templates/grabber.html"
        icon = "grip"
        abstract = True
