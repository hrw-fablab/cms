from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import InlinePanel

from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


from modelcluster.models import ClusterableModel

from organisation.models import Person

class Organisation(ClusterableModel, models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
    
    panels = [
        FieldPanel("name", heading="Organisation"),
        InlinePanel("related_projects", heading="Projekte"),
    ]

    @property
    def Projektanzahl(self):
        return self.related_projects.count()

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisationen"
