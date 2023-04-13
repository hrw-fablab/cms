from wagtail import blocks


class EventsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "blocks/events.html"
        icon = "date"
