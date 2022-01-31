from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
    InlinePanel,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

class Sponsor(Orderable):
    logo = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    logo_alt = models.CharField(max_length=255, null=True, blank=True)

    page = ParentalKey("SiteSettings", on_delete=models.CASCADE, related_name="sponsor")

    panels = [
        ImageChooserPanel("logo"),
        FieldPanel("logo_alt"),
    ]


class Social(Orderable):
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    page = ParentalKey("SiteSettings", on_delete=models.CASCADE, related_name="social")

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
    ]


@register_setting
class SiteSettings(BaseSetting, ClusterableModel):
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

    logo = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    logo_title = models.CharField(max_length=30, null=True, blank=True)

    brand_color = ColorField(null=True, blank=True)
    text_color = ColorField(null=True, blank=True)

    surface_color_one = ColorField(null=True, blank=True)
    surface_color_two = ColorField(null=True, blank=True)

    intern_website = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("logo"),
                FieldPanel("logo_title"),
            ],
            heading="Logo",
            classname="collapsible",
        ),
        MultiFieldPanel(
            [
                NativeColorPanel("brand_color"),
                NativeColorPanel("text_color"),
                NativeColorPanel("surface_color_one"),
                NativeColorPanel("surface_color_two"),
            ],
            heading="Brand Farben",
            classname="collapsible",
        ),
        MultiFieldPanel(
            [
                FieldPanel("street"),
                FieldPanel("housenumber"),
                FieldPanel("city"),
                FieldPanel("plz"),
                FieldPanel("email"),
            ],
            heading="Adress",
            classname="collapsible",
        ),
        MultiFieldPanel(
            [
                PageChooserPanel("contact"),
                PageChooserPanel("impressum"),
                PageChooserPanel("data_protection"),
            ],
            heading="Service",
            classname="collapsible",
        ),
        InlinePanel("sponsor", label="Sponsoren"),
        InlinePanel("social", label="Social Media"),
        PageChooserPanel("intern_website"),
    ]

    class Meta:
        verbose_name = "Seiten Konfiguration"
