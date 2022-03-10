from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from datetime import date


class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
    ]

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
        PageChooserPanel("grabber"),
        FieldPanel("title"),
        FieldPanel("amount"),
    ]

    class Meta:
        abstract = True
