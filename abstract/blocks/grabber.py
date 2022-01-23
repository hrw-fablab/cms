from wagtail.core import blocks
from wagtail.core.blocks.field_block import PageChooserBlock


class GrabberBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    pages = blocks.ListBlock(PageChooserBlock())

    class Meta:
        group = "Cointainer"
        template = "templates/grabber.html"
        icon = "grip"
        abstract = True
