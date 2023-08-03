from wagtail import blocks


class HeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "blocks/heading.html"
        icon = "title"
