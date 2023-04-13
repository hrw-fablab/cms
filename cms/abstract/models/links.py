from operator import mod
from django.db import models
from wagtail.admin.panels import FieldPanel
from datetime import date

CATEGORYCHOICES = (
    ("none", "none"),
    ("teach", "Lehre"),
    ("open", "Offenes Angebot"),
    ("school", "Schülerkurse"),
    ("workshop", "Workshop"),
    ("extern", "Extern"),
    ("event", "FabLab Event"),
)


class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORYCHOICES, default="none", max_length=255)

    panels = [FieldPanel("url"), FieldPanel("title"), FieldPanel("category")]

    class Meta:
        abstract = True


class ExpireLink(Link):
    expire = models.DateField(null=True, blank=True)

    @property
    def is_visible(self):
        return date.today() > self.expire

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
        FieldPanel("category"),
        FieldPanel("expire"),
    ]

    class Meta:
        abstract = True


class PageLink(models.Model):
    grabber = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    title = models.CharField(max_length=255, null=True)
    amount = models.IntegerField()

    panels = [
        FieldPanel("grabber"),
        FieldPanel("title"),
        FieldPanel("amount"),
    ]

    class Meta:
        abstract = True
