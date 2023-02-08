from wagtail.models import Orderable
from django.db import models

from wagtail.admin.panels import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import StreamField

from modelcluster.fields import ParentalKey

from abstract.models.links import Link

from blocks.models import ProjectBlock
from core.models import FablabBasePage


class ProjectPageLink(Orderable, Link):
    page = ParentalKey(
        "ProjectPage", on_delete=models.CASCADE, related_name="project_links"
    )


class ProjectPage(FablabBasePage):
    template = "pages/project.html"

    parent_page_types = ["ProjectIndexPage"]
    subpage_type = []

    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    date = models.DateField()

    introduction = models.CharField(max_length=255)

    body = StreamField(ProjectBlock(), blank=True, use_json_field=True)

    content_panels = FablabBasePage.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("date"),
            ],
            heading="Hero",
        ),
        FieldPanel("introduction"),
        InlinePanel("project_links", label="Project Links"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Projekt"
