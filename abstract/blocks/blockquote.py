from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BlockquoteBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    text = blocks.TextBlock(required=False)
    cite = blocks.CharBlock(required=False)

    class Meta:
        template = "molecules/blockquote.html"
        icon = "openquote"
        abstract = True
