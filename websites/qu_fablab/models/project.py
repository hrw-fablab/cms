from modelcluster.fields import ParentalKey
from wagtail.core import models
from wagtail.core.models import Orderable
from django.db import models
from wagtail.core.models.i18n import TranslatableMixin
from abstract.pages.project import AbstractProjectPage
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from ..blocks import ProjectBlock

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

class QuProjectPage(AbstractProjectPage):
    template = "pages/project.html"

    parent_page_types = ["QuIndexCategoryPage"]
    subpage_type = []

    body = StreamField(ProjectBlock())

    content_panels = AbstractProjectPage.content_panels + [
        InlinePanel("page_link", label="Project Links"),
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Projekt Seite"
