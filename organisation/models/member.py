from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey
from chooser.widgets import PersonChooser

from modelcluster.models import ClusterableModel


class Member(ClusterableModel, models.Model):
    person = models.ForeignKey(
        "organisation.Person",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    role = models.ForeignKey(
        "organisation.Role",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("person", widget=PersonChooser, heading="Mitglied"),
        FieldPanel("role"),
    ]

    link = ParentalKey(
        "organisation.Project",
        on_delete=models.CASCADE,
        related_name="related_member",
    )

    class Meta:
        verbose_name = "Mitglied"
        verbose_name_plural = "Mitglieder"
