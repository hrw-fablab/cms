from wagtail.core import blocks


class HeadingBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        abstract = True
