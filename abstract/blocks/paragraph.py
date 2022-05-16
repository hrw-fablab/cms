from wagtail import blocks


class ParagraphBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(
        features=[
            "bold",
            "italic",
            "h3",
            "ul",
            "link",
            "document-link",
            "image",
            "embed",
        ]
    )

    class Meta:
        template = "molecules/paragraph.html"
        icon = "doc-full"
        abstract = True
