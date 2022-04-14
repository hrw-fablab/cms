from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from core.models import FablabBasePage

class AbstractProjectPage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    date = models.DateField()

    introduction = models.CharField(max_length=255)

    content_panels = FablabBasePage.content_panels + [
        MultiFieldPanel([
            FieldPanel("image"),
            FieldPanel("date"),
        ], heading="Hero"),
        FieldPanel("introduction"),
    ]

    class Meta:
        verbose_name = "Projekt"
        abstract = True