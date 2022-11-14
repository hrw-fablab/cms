import datetime
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from modelcluster.models import ClusterableModel
from wagtail.search.index import Indexed, SearchField
import calendar

REAPEATCHOICES = (
    ("0", "none"),
    ("1", "weekly"),
)

CATEGORYCHOICES = (
    ("none", "none"),
    ("teach", "Lehre"),
    ("open", "Offenes Angebot"),
    ("student", "Schülerkurse"),
    ("workshop", "Workshop"),
    ("external", "Extern"),
    ("6", "FabLab Event"),
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


class Event(Indexed, ClusterableModel):
    title = models.CharField("Titel", max_length=60, null=True, blank=True)
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
                FieldPanel("category"),
            ],
            heading="Informationen",
        ),
        FieldRowPanel(
            [
                FieldPanel("link", heading="url"),
                FieldPanel("link_text", heading="text"),
            ],
            heading="Link",
        ),
        FieldRowPanel(
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
        InlinePanel("related_expection", heading="Ausnahmen", label="Ausnahme"),
    ]

    search_fields = [
        SearchField("title", partial_match=True),
    ]

    @property
    def name(self):
        return "{}".format(self.title)

    @property
    def length(self):
        return int(self.end.day - self.start.day)

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

    def visible_calendar(self, date):
        if self.repeat == "0":
            start = datetime.date(self.start.year, self.start.month, 1)
            end = datetime.date(self.end.year, self.end.month, 2)
            if start <= date <= end:
                return True
        else:
            start = datetime.date(self.repeatStart.year, self.repeatStart.month, 1)
            end = datetime.date(self.repeatEnd.year, self.repeatEnd.month, 2)
            if start <= date <= end:
                return True
        return False

    def visible_events(self, date):
        if self.repeat == "0":
            start = datetime.date(self.start.year, self.start.month, self.start.day)
            end = datetime.date(
                self.end.year,
                self.end.month,
                calendar.monthrange(self.end.year, self.end.month)[1],
            )
            if start >= date <= end:
                return True
        else:
            start = datetime.date(
                self.repeatStart.year, self.repeatStart.month, self.repeatStart.day
            )
            end = datetime.date(
                self.repeatEnd.year, self.repeatEnd.month, self.repeatEnd.day
            )
            if start <= date <= end:
                return True
        return False

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
