from wagtail.core import blocks


class HeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "molecules/heading.html"
        icon = "title"
        abstract = True
