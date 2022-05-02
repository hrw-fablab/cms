from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from chooser.widgets import ProjectChooser
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class Area(ClusterableModel):
    project = models.ForeignKey(
        "organisation.Project",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [FieldPanel("project", widget=ProjectChooser, heading="Projekt")]

    link = ParentalKey(
        "organisation.Organisation",
        on_delete=models.CASCADE,
        related_name="related_projects",
    )

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekte"
