from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.TextBlock(required=False, max_length=255)
    image = ImageChooserBlock(required=False)
    video = VideoChooserBlock(required=False, icon="media")

    class Meta:
        template = "blocks/hero.html"
