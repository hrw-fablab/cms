from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    text = blocks.TextBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    link = blocks.URLBlock(
        required=False,
        help_text="""Wenn die Seite extern ist oder es sich um ein Dokument handelt. 
        Muss die url angeben werden""",
    )
    new_tab = blocks.BooleanBlock(
        required=False,
        help_text="Wenn die neue Seite in einen neuen Tab geöffnet werden soll",
    )

    class Meta:
        template = "blocks/card.html"
        icon = "doc-full"
