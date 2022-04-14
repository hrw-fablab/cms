from wagtail import blocks


class HeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "atoms/heading.html"
        icon = "title"
        abstract = True
