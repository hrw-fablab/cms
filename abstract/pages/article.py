from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from core.models import FablabBasePage


class AbstractArticlePage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    author = models.ForeignKey(
        "snippets.Author",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    tag = models.ForeignKey(
        "snippets.Tag",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    date = models.DateField()

    introduction = models.CharField(max_length=255)

    body = RichTextField(
        features=[
            "bold",
            "italic",
            "h3",
            "ul",
            "link",
            "document-link",
            "image",
            "embed",
        ]
    )

    content_panels = FablabBasePage.content_panels + [
        ImageChooserPanel("image"),
        SnippetChooserPanel("author"),
        SnippetChooserPanel("tag"),
        FieldPanel("date"),
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True
