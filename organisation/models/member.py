from django.db import models
from wagtail.admin.panels import FieldPanel

from modelcluster.fields import ParentalKey

from modelcluster.models import ClusterableModel

from organisation.models import Role


class FilteredPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            filtered = Role.objects.filter(link_id=self.instance.link_id)
            self.form.fields["role"].queryset = filtered


class Member(ClusterableModel):
    person = models.ForeignKey(
        "organisation.Person",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    link = ParentalKey(
        "organisation.Project",
        on_delete=models.CASCADE,
        related_name="related_member",
    )

    role = models.ForeignKey(
        "organisation.Role",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("person"),
        FilteredPanel("role"),
    ]

    class Meta:
        verbose_name = "Mitglied"
        verbose_name_plural = "Mitglieder"
