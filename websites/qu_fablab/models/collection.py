<<<<<<< Updated upstream
=======
from pydoc import classname
>>>>>>> Stashed changes
from django.db import models

from core.models import FablabBasePage

from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
<<<<<<< Updated upstream
=======
    PageChooserPanel
>>>>>>> Stashed changes
)

from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from datetime import date

<<<<<<< Updated upstream
class Link(models.Model):
=======
class Link(Orderable):
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
    class Meta:
        abstract = True

class LinkCollections(Orderable, Link):
    parent = ParentalKey("QuCollectionPage", on_delete=models.CASCADE, related_name="link")
=======
class Page(Orderable):
    page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    amount = models.IntegerField()

    parent = ParentalKey("QuCollectionPage", on_delete=models.CASCADE, related_name="collection_page")

    panels = [
        PageChooserPanel("page"),
        FieldPanel("amount")
    ]

>>>>>>> Stashed changes

class QuCollectionPage(FablabBasePage, ClusterableModel):
    template = "pages/collection.html"
    
    content_panels = FablabBasePage.content_panels + [
<<<<<<< Updated upstream
        InlinePanel("link", label="Link"),
=======
        InlinePanel("collection_link", label="Link", classname="collabsible"),
        InlinePanel("collection_page", label="Page", classname="collabsible"),
>>>>>>> Stashed changes
    ]
