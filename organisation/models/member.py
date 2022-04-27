from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey
from chooser.widgets import PersonChooser

from modelcluster.models import ClusterableModel

from organisation.models import Role


class FilteredPanel(FieldPanel):
    def on_form_bound(self):
        try:
            if self.instance.link_id == None:
                list = self.request.path_info.split("/")
                id = int(list[len(list) - 2])
                filtered = Role.objects.filter(link_id=id)
            else:
                filtered = Role.objects.filter(link_id=self.instance.link_id)
        except:
            self.form[self.field_name]
        finally:
            self.form.fields["role"].queryset = filtered
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
