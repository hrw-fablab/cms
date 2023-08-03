from wagtail import blocks


class HTMLBlock(blocks.StructBlock):
    code = blocks.RawHTMLBlock(required=False)

    class Meta:
        template = "blocks/html.html"
        icon = "image"
