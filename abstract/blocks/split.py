from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock


class SplitBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.RichTextBlock(
        required=False,
        features=[
            "bold",
            "italic",
            "ul",
        ],
    )
    link = LinkBlock(required=False)
    image = ImageChooserBlock(required=False)
    video = VideoChooserBlock(required=False)

    class Meta:
        template = "organisms/split.html"
        abstract = True
