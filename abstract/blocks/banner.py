from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    link = LinkBlock(required=False)

    class Meta:
        template = "organisms/banner.html"
        abstract = True
