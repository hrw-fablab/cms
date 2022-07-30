from operator import mod
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.models import ClusterableModel


REAPEATCHOICES = (
    ("0", "none"),
    ("1", "weekly"),
)

CATEGORYCHOICES = (
    ("0", "none"),
    ("1", "Lehre"),
    ("2", "Offenes Angebot"),
    ("3", "Schülerkurse"),
    ("4", "Workshop"),
    ("5", "Extern"),
)

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class Expection(ClusterableModel):
    start = models.DateField()
    end = models.DateField()

    link = ParentalKey(
        "organisation.Event",
        on_delete=models.CASCADE,
        related_name="related_expection",
    )

    panels = [
        FieldPanel("start"),
        FieldPanel("end"),
    ]


class Event(ClusterableModel):
    title = models.CharField("Titel", max_length=30, null=True, blank=True)
    adress = models.CharField("Adresse", max_length=60, null=True, blank=True)
    description = models.TextField(
        "Beschreibung", max_length=140, null=True, blank=True
    )
    link = models.URLField("Link", blank=True, null=True)
    link_text = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=255, choices=CATEGORYCHOICES, default="none")

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
                MultiFieldPanel(
                    [
                        FieldPanel("link"),
                        FieldPanel("link_text"),
                    ],
                    heading="Link",
                ),
                FieldPanel("category"),
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
        InlinePanel("related_expection", heading="Expections"),
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

    def visible_year(self, date):
        if (self.repeatStart == None or self.repeatEnd == None) and self.repeat != "0":
            return True

        if self.repeat == "0":
            if (
                self.start.replace(tzinfo=None).year < date.year
                or self.end.replace(tzinfo=None).year > date.year
            ):
                return False

            return True
        else:
            if self.repeatStart.year < date.year or self.repeatEnd.year > date.year:
                return False

            return True

    def visible_month(self, date):
        if (self.repeatStart == None or self.repeatEnd == None) and self.repeat != "0":
            return True

        if self.repeat == "0":
            if (
                self.start.replace(tzinfo=None).month < date.month
                or self.end.replace(tzinfo=None).month > date.month
            ):
                return False

            return True
        else:
            if self.repeatStart.month > date.month or self.repeatEnd.month < date.month:
                return False

            return True

    def visible_day(self, date):
        if (self.repeatStart == None or self.repeatEnd == None) and self.repeat != "0":
            return True

        if self.repeat == "0":
            if self.start.replace(tzinfo=None).day < date.day:
                return False

            return True
        else:
            if self.repeatStart.day < date.day or self.repeatEnd.day < date.day:
                return False

            return True

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
