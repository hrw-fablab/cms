from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Person(index.Indexed, ClusterableModel):
    name = models.CharField("First name", max_length=254)

    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    employment = models.CharField(max_length=254)
    link = models.URLField(max_length=254, null=True, blank=True)
    since = models.DateField()
    career = models.CharField(max_length=254, null=True, blank=True)
    responsibility = models.CharField(max_length=254, null=True, blank=True)
    expert = models.CharField(max_length=254, null=True, blank=True)
    projects = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=254, null=True, blank=True)

    panels = [
        FieldPanel("name"),
        ImageChooserPanel("image"),
        FieldPanel("employment"),
        FieldPanel("link"),
        FieldPanel("since"),
        FieldPanel("career"),
        FieldPanel("responsibility"),
        FieldPanel("expert"),
        FieldPanel("projects"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
