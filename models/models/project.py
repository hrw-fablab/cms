from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import InlinePanel

from modelcluster.models import ClusterableModel

class Project(ClusterableModel, models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    panels = [FieldPanel("name"), InlinePanel("related_member", heading="Mitglieder")]
