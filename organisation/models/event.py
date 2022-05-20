from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from modelcluster.models import ClusterableModel


REAPEATCHOICES = (
    ("0", "none"),
    ("1", "weekly"),
)


class Event(ClusterableModel):
    title = models.CharField("Titel", max_length=30, null=True, blank=True)
    adress = models.CharField("Adresse", max_length=60, null=True, blank=True)
    description = models.CharField(
        "Beschreibung", max_length=140, null=True, blank=True
    )
    link = models.URLField("Link", blank=True, null=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    repeat = models.CharField(max_length=255, choices=REAPEATCHOICES, default="none")
    repeatStart = models.DateField("Von", null=True, blank=True)
    repeatEnd = models.DateField("Bis", null=True, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("adress"),
                FieldPanel("description"),
                FieldPanel("link"),
            ],
            heading="Informationen",
        ),
        MultiFieldPanel(
            [
                FieldPanel("start"),
                FieldPanel("end"),
            ],
            heading="Zeit",
        ),
        MultiFieldPanel(
            [
                FieldPanel("repeat"),
                FieldPanel("repeatStart"),
                FieldPanel("repeatEnd"),
            ],
            heading="Wiederholung",
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

    @property
    def timeStart(self):
        return self.start.strftime("%H:%M")

    @property
    def timeEnd(self):
        return self.end.strftime("%H:%M")

    def visible(self, date):
        if self.repeat == "0":
            if (
                self.end.replace(tzinfo=None).year < date.year
                or self.start.replace(tzinfo=None).year > date.year
            ):
                return False

            if (
                self.start.replace(tzinfo=None).month < date.month
                or self.end.replace(tzinfo=None).month > date.month
            ):
                return False

            return True
        else:
            if self.repeatEnd.year < date.year or self.repeatStart.year > date.year:
                return False

            if self.repeatStart.month > date.month or self.repeatEnd.month < date.month:
                return False
            return True

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
