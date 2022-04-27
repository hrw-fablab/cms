from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from datetime import datetime, tzinfo

from pytz import utc


class Event(ClusterableModel, models.Model):
    title = models.CharField("Titel", max_length=100, null=True, blank=True)
    adress = models.CharField("Adresse", max_length=250, null=True, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    repeat = models.IntegerField("Wiederholen", null=True, blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("adress"),
        MultiFieldPanel(
            [
                FieldPanel("start"),
                FieldPanel("end"),
                FieldPanel("repeat"),
            ],
            heading="Zeit",
        ),
    ]

    @property
    def name(self):
        return "{}".format(self.title)

    @property
    def year(self):
        return int(self.start.strftime("%Y"))

    @property
    def month(self):
        return int(self.start.strftime("%m"))

    def visible(self, date):
        if (
            self.start.replace(tzinfo=None) <= date
            and self.end.replace(tzinfo=None) >= date
        ):
            return True
        return False

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
