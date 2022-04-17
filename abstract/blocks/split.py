from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks.field_block import PageChooserBlock


class SplitBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.RichTextBlock(
        required=False,
        features=[
            "bold",
            "italic",
            "ul",
            "link",
        ],
    )
    page = PageChooserBlock(required=False)
    image = ImageChooserBlock(required=False)
    accent = blocks.BooleanBlock(required=False)

    class Meta:
        template = "organisms/split.html"
        abstract = True
