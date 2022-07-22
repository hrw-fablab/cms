from wagtail import blocks


class CallBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = blocks.TextBlock(required=False, max_length=140)
    link_text = blocks.CharBlock(required=False)
    page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "molecules/call.html"
        abstract = True
