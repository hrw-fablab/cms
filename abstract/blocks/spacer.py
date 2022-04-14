from wagtail import blocks


class SpacerBlock(blocks.StaticBlock):
    class Meta:
        template = "atoms/spacer.html"
        icon = "arrows-up-down"
        abstract = True
