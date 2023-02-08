from wagtail.models import Orderable
from django.db import models

from wagtail.admin.panels import (
    InlinePanel,
)

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from abstract.pages.base import AbstractBasePage

from abstract.models.links import ExpireLink, PageLink

from core.models import FablabBasePage


class CollectionPagePage(Orderable, PageLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_pages"
    )


class CollectionPageLink(Orderable, ExpireLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_links"
    )


class CollectionPage(FablabBasePage, ClusterableModel):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/collection.html"

    content_panels = AbstractBasePage.content_panels + [
        InlinePanel("collection_links", label="Link", classname="collabsible"),
        InlinePanel("collection_pages", label="Page", classname="collabsible"),
    ]

    class Meta:
        verbose_name = "Link Sammlung"
