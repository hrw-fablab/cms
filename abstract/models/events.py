from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    date = models.DateField()
    introduction = models.CharField(max_length=100)
    body = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
        ImageChooserPanel("image"),
        FieldPanel("date"),
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True
