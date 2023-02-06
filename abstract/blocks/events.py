from wagtail import blocks


class EventsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "organisms/events.html"
        icon = "date"
        abstract = True
