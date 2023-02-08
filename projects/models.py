from django.db import models

from wagtail.admin.panels import InlinePanel, FieldPanel

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


class Project(ClusterableModel):
    name = models.CharField(max_length=254, null=True, blank=True)

    panels = [
        FieldPanel("name", heading="Projektname"),
        InlinePanel("related_roles", heading="Projektrollen"),
        InlinePanel("related_member", heading="Mitglieder"),
    ]

    @property
    def Personenanzahl(self):
        return self.related_member.count()

    @property
    def members_ordered(self):
        ordered_list = []
        for role in self.related_roles.all():
            for member in self.related_member.all():
                if member.role == role:
                    ordered_list.append(member)

        for member in self.related_member.all():
            if member.role == None:
                ordered_list.append(member)

        return ordered_list

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekte"
