from django.db import models
from django.db.models.fields import IntegerField

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from core.models import FablabBasePage
from organisation.widgets import DeviceCategoryChooser


class AbstractDevicePage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    category = models.ForeignKey(
        "organisation.DeviceCategory",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    number = IntegerField()

    introduction = models.CharField(max_length=255)

    content_panels = FablabBasePage.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("number"),
                FieldPanel("category", widget=DeviceCategoryChooser)
            ],
            heading="Hero",
        ),
        FieldPanel("introduction"),
    ]

    class Meta:
        verbose_name = "Gerät"
        abstract = True
