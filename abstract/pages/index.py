from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from core.models import FablabBasePage


class AbstractIndexPage(FablabBasePage):
    heading = models.CharField(max_length=255, blank=True)

    content_panels = FablabBasePage.content_panels + [
        FieldPanel("heading"),
    ]

    class Meta:
        abstract = True
