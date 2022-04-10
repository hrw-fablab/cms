from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from models.widgets import PersonChooser


class Member(models.Model):
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
