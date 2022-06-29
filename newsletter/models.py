from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign, Contact

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField

class Newsletter(Campaign):
    headline = models.CharField(
        max_length=255,
        help_text="The headline to use for the newsletter."
    )

    body = StreamField(DefaultBlocks())

    panels = Campaign.panels + [
        FieldPanel("headline"),
        StreamFieldPanel("body"),
    ]

class Contact(Contact):
    pass