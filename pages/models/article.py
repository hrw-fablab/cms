from django.db import models
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from core.models import FablabBasePage


class ArticlePage(FablabBasePage):
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    date = models.DateField()

    organisation = models.ForeignKey(
        "organisation.Organisation",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    author = models.ForeignKey(
        "organisation.Person",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    introduction = models.CharField(max_length=150)

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
        FieldPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("author"),
            ],
            heading="Informationen",
        ),
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Artikel"
