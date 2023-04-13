from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/banner.html"
