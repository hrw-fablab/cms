from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from core.models import FablabBasePage

class AbstractProjectPage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    category = models.ForeignKey(
        "snippets.ProjectCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    date = models.DateField()

    introduction = models.CharField(max_length=255)

    content_panels = FablabBasePage.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel("image"),
            SnippetChooserPanel("category"),
            FieldPanel("date"),
        ], heading="Hero"),
        FieldPanel("introduction"),
    ]

    class Meta:
        verbose_name = "Projekt"
        abstract = True