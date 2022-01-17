from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock


class MediaBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    video = VideoChooserBlock(required=False, icon="media")

    class Meta:
        icon = "media"
        abstract = True
