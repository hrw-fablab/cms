from django.db import models
import requests
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey
from chooser.widgets import PersonChooser

from modelcluster.models import ClusterableModel

from organisation.models import Role
from organisation.models import Project


class FilteredPanel(FieldPanel):
    def on_form_bound(self):
        try:
            list = self.request.path_info.split("/")
            id = int(list[len(list) - 2])
            roles = Role.objects.filter(link_id = id)
            self.form.fields["role"].queryset = roles
        except:
            self.form[self.field_name]
        finally:
            super().on_form_bound()


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
        FieldPanel("person", widget=PersonChooser, heading="Mitglied"),
        FilteredPanel("role"),
    ]

    class Meta:
        verbose_name = "Mitglied"
        verbose_name_plural = "Mitglieder"
