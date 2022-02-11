from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock
from wagtail.core.blocks.field_block import PageChooserBlock


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
    page = PageChooserBlock(required=False)
    image = ImageChooserBlock(required=False)
    video = VideoChooserBlock(required=False)

    class Meta:
        template = "organisms/split.html"
        abstract = True
