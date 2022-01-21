from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class Footer(BaseSetting):
    street = models.CharField(max_length=255, null=True, blank=True)
    housenumber = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    plz = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    contact = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    impressum = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    data_protection = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    thingiverse = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("street"),
                FieldPanel("housenumber"),
                FieldPanel("city"),
                FieldPanel("plz"),
                FieldPanel("email"),
            ],
            heading="Adress",
        ),
        MultiFieldPanel(
            [
                PageChooserPanel("contact"),
                PageChooserPanel("impressum"),
                PageChooserPanel("data_protection"),
            ],
            heading="Service",
        ),
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("instagram"),
                FieldPanel("youtube"),
                FieldPanel("thingiverse"),
                FieldPanel("twitter"),
            ],
            heading="Social Media",
        ),
    ]
