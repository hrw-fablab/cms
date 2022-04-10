from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from site_chooser.widgets import PersonChooser


class Project(models.Model):
    name = models.CharField("Project Name", max_length=254)

    person = models.ForeignKey(
        "site_models.Person",
        related_name="Person",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [FieldPanel("person", widget=PersonChooser)]


class Person(models.Model):
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
