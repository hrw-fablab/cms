from django.db import models

from core.models import FablabBasePage

from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
)

from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from datetime import date

class Link(models.Model):
    url = models.URLField(max_length=255)

    title = models.CharField(max_length=255)

    expire = models.DateField(null=True, blank=True)

    @property
    def is_visible(self):
        return date.today() < self.expire

    parent = ParentalKey("QuCollectionPage", on_delete=models.CASCADE, related_name="collection_link")

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
        FieldPanel("expire"),
    ]

    class Meta:
        abstract = True

class LinkCollections(Orderable, Link):
    parent = ParentalKey("QuCollectionPage", on_delete=models.CASCADE, related_name="link")

class QuCollectionPage(FablabBasePage, ClusterableModel):
    template = "pages/collection.html"
    
    content_panels = FablabBasePage.content_panels + [
        InlinePanel("link", label="Link"),
    ]
