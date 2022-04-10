from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class Person(models.Model):
    first_name = models.CharField("First Name", max_length=254)
    last_name = models.CharField("Last Name", max_length=254)

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
        MultiFieldPanel(
            [
                FieldPanel("first_name"),
                FieldPanel("last_name"),
            ],
            heading="Name",
        ),
        ImageChooserPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("employment"),
                FieldPanel("link"),
                FieldPanel("since"),
                FieldPanel("career"),
                FieldPanel("responsibility"),
                FieldPanel("expert"),
                FieldPanel("projects"),
            ],
            heading="Information",
        ),
        FieldPanel("description"),
    ]

