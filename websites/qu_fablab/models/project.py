from modelcluster.fields import ParentalKey
from wagtail.core import models
from wagtail.core.models import Orderable
from django.db import models
from wagtail.core.models.i18n import TranslatableMixin
from abstract.pages.project import AbstractProjectPage
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ProjectPageLink(TranslatableMixin, Orderable):
    page = ParentalKey(
        "QuProjectPage", on_delete=models.CASCADE, related_name="page_link"
    )
    link_url = models.URLField()
    link_title = models.CharField(max_length=255)

    panels = [
        FieldPanel("link_url"),
        FieldPanel("link_title"),
    ]


class ProjectAuthor(TranslatableMixin, Orderable):
    page = ParentalKey(
        "QuProjectPage", on_delete=models.CASCADE, related_name="project_author"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        ImageChooserPanel("image"),
    ]


class QuProjectPage(AbstractProjectPage):
    template = "pages/project.html"

    parent_page_types = ["QuIndexCategoryPage"]
    subpage_type = []

    content_panels = AbstractProjectPage.content_panels + [
        InlinePanel("page_link", label="Project Links"),
        InlinePanel("project_author", label="Project Authors"),
    ]

    class Meta:
        verbose_name = "Projekt Seite"
