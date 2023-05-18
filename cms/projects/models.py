from django.db import models

from wagtail.admin.panels import InlinePanel, FieldPanel, MultipleChooserPanel

from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey


class Role(Orderable):
    name = models.CharField(max_length=254, null=True, blank=True)
    visible = models.BooleanField(default=True)

    link = ParentalKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="related_roles",
    )

    def __str__(self):
        return "{}".format(self.name)


class FilteredPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            filtered = Role.objects.filter(link_id=self.instance.link_id)
            self.form.fields["role"].queryset = filtered


class Member(ClusterableModel):
    person = models.ForeignKey(
        "persons.Person",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    link = ParentalKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="related_member",
    )

    role = models.ForeignKey(
        "projects.Role",
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


class Project(ClusterableModel):
    name = models.CharField(max_length=254, null=True, blank=True)

    panels = [
        FieldPanel("name", heading="Projektname"),
        InlinePanel("related_roles", heading="Projektrollen"),
        MultipleChooserPanel("related_member", chooser_field_name="person"),
    ]

    @property
    def members_amount(self):
        return self.related_member.count()

    @property
    def members_ordered(self):
        ordered_list = []
        for role in self.related_roles.all():
            for member in self.related_member.all():
                if member.role == role:
                    ordered_list.append(member)

        for member in self.related_member.all():
            if member.role is None:
                ordered_list.append(member)

        return ordered_list

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekte"
