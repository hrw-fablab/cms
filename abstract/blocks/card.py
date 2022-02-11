from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.field_block import PageChooserBlock

class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=False)
    text = blocks.TextBlock(required=False)
    link = PageChooserBlock(required=False)

    class Meta:
        template = "templates/card.html"
        icon = "doc-full"
        abstract = True