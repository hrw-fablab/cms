from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import InlinePanel

from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel

class Organisation(ClusterableModel, models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisationen"
