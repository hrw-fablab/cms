from wagtail import blocks


class CalendarBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    class Meta:
        template = "organisms/calendar.html"
        icon = "date"
