from django.db import models

from core.models import FablabBasePage

from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel
)

from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from datetime import date


class Link(Orderable):
    url = models.URLField(max_length=255)

    title = models.CharField(max_length=255)

    expire = models.DateField(null=True, blank=True)

    @property
    def is_visible(self):
        return date.today() < self.expire

    parent = ParentalKey("CollectionPage", on_delete=models.CASCADE, related_name="collection_link")

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
        FieldPanel("expire"),
    ]

class Page(Orderable):
    page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    amount = models.IntegerField()

    parent = ParentalKey("CollectionPage", on_delete=models.CASCADE, related_name="collection_page")

    panels = [
        PageChooserPanel("page"),
        FieldPanel("amount")
    ]

class CollectionPage(FablabBasePage, ClusterableModel):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/collection.html"
    
    content_panels = FablabBasePage.content_panels + [
        InlinePanel("collection_link", label="Link", classname="collabsible"),
        InlinePanel("collection_page", label="Page", classname="collabsible"),
    ]
