from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    video = VideoChooserBlock(required=False, icon="media")

    class Meta:
        template = "organisms/hero.html"
        abstract = True
