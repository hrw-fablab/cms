from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class SplitBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    text = blocks.RichTextBlock(
        required=False,
        features=[
            "bold",
            "italic",
            "ul",
            "document-link",
            "link",
        ],
    )
    page = blocks.PageChooserBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/split.html"
