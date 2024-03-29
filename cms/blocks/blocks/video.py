from wagtail import blocks
from wagtailmedia.blocks import VideoChooserBlock


class VideoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    video = VideoChooserBlock(required=False, icon="media")

    class Meta:
        template = "molecules/media.html"
        icon = "media"
