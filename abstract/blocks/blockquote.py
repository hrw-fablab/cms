from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BlockquoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    cite = blocks.CharBlock(required=False)

    class Meta:
        template = "molecules/blockquote.html"
        icon = "openquote"
        abstract = True
