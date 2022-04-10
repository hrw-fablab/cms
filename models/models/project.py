from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from django.db import models

from wagtail.admin.edit_handlers import InlinePanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from chooser.widgets import PersonChooser

class Member(Orderable):
    member = models.ForeignKey(
        "models.Person",
        related_name="member",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [FieldPanel("member", widget=PersonChooser)]

    link = ParentalKey(
        "models.Project", on_delete=models.CASCADE, related_name="related_member"
    )


class Project(ClusterableModel, models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    panels = [FieldPanel("name"), InlinePanel("related_member")]
