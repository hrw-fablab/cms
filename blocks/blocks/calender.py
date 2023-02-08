from wagtail import blocks


class CalendarBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    events = blocks.BooleanBlock(required=False)

    class Meta:
        template = "organisms/calendar.html"
        icon = "date"
