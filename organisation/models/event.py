from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class Event(ClusterableModel, models.Model):
    title = models.CharField("Titel", max_length=30, null=True, blank=True)
    adress = models.CharField("Adresse", max_length=60, null=True, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    repeat = models.IntegerField("Wiederholen", null=True, blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("adress"),
        FieldPanel("description"),
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
    def length(self):
        time = self.end - self.start
        if time.days <= 1:
            return 1
        return int(time.days)

    @property
    def year(self):
        return int(self.start.strftime("%Y"))

    @property
    def month(self):
        return int(self.start.strftime("%m"))

    @property
    def day(self):
        return int(self.start.strftime("%d"))

    def visible(self, date):
        if (
            self.end.replace(tzinfo=None).year < date.year
            or self.start.replace(tzinfo=None).year > date.year
        ):
            return False

        if (
            self.start.replace(tzinfo=None).month < date.month
            or self.start.replace(tzinfo=None).month > date.month
        ):
            return False

        return True

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
