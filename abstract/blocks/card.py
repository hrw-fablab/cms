from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock

class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=False)
    text = blocks.TextBlock(required=False)
    link = LinkBlock(required=False)

    class Meta:
        template = "templates/card.html"
        icon = "doc-full"
        abstract = True