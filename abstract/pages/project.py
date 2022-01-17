from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
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

    body = RichTextField(features=["h3", "ul", "link", "image", "embed"])

    content_panels = FablabBasePage.content_panels + [
        ImageChooserPanel("image"),
        SnippetChooserPanel("category"),
        FieldPanel("date"),
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True
