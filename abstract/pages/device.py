from django.db import models
from django.db.models.fields import IntegerField

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from core.models import FablabBasePage


class AbstractDevicePage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    number = IntegerField()

    category = models.ForeignKey(
        "snippets.DeviceCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    introduction = models.CharField(max_length=255)

    content_panels = FablabBasePage.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("image"),
                FieldPanel("number"),
                SnippetChooserPanel("category"),
            ],
            heading="Hero",
        ),
        FieldPanel("introduction"),
    ]

    class Meta:
        verbose_name = "Gerät"
        abstract = True
