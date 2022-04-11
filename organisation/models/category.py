from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class Category(models.Model):
    name = models.CharField("Name der Kategorie", max_length=254)

    panels = [
        FieldPanel("name"),
    ]


class DeviceCategory(Category):
    class Meta:
        verbose_name = "Gerätekategorie"
        verbose_name_plural = "Gerätekategorien"


class ProjectCategory(Category):
    class Meta:
        verbose_name = "Projektkategorie"
        verbose_name_plural = "Projektkategorien"
