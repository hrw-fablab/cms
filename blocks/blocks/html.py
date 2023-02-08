from wagtail import blocks


class HTMLBlock(blocks.StructBlock):
    code = blocks.RawHTMLBlock(required=False)

    class Meta:
        template = "organisms/html.html"
        icon = "image"
