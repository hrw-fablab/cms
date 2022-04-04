from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    illustration = blocks.BooleanBlock(required=False)

    class Meta:
        template = "organisms/banner.html"
        abstract = True
