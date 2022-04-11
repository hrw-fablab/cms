from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class Category(models.Model):
    name = models.CharField("Name der Kategorie", max_length=254)

    panels = [
        FieldPanel("name"),
    ]


class DeviceCategory(Category):
    pass


class ProjectCategory(Category):
    pass
