from django.db import models
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from chooser.widgets import PersonChooser

from core.models import FablabBasePage
from wagtail.core.models import Page


class AbstractArticlePage(FablabBasePage):
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
        ImageChooserPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("author", widget=PersonChooser),
            ],
            heading="Informationen",
        ),
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        parent = Page.get_parent(self)
        context["parent"] = parent
        return context

    class Meta:
        verbose_name = "Artikel"
        abstract = True
