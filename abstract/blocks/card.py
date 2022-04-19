from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    text = blocks.TextBlock(required=False)
    page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "templates/card.html"
        icon = "doc-full"
        abstract = True
