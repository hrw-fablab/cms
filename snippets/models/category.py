from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
)


class DeviceCategory(models.Model):
    name = models.CharField("Category Name", max_length=255, blank=False)

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gerätekategorie"
        verbose_name_plural = "Gerätekategorien"


class ProjectCategory(models.Model):
    name = models.CharField("Category Name", max_length=255, blank=False)

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Projektkategorie"
        verbose_name_plural = "Projektkategorien"
