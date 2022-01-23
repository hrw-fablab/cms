from wagtail.core import blocks


class SpacerBlock(blocks.StructBlock):
    class Meta:
        template = "atoms/spacer.html"
        icon = "arrows-up-down"
        abstract = True
