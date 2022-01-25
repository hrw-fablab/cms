from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "organisms/banner.html"
        abstract = True
