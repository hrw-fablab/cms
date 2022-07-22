from django.db import models
from wagtail.admin.panels import (
    MultiFieldPanel,
    FieldPanel,
    InlinePanel,
    TabbedInterface,
    ObjectList,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.models import ClusterableModel

from wagtail.models import Orderable
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

    logo_en = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    logo_alt_en = models.CharField(max_length=255, null=True, blank=True)

    page = ParentalKey(
        "GlobalSettings", on_delete=models.CASCADE, related_name="sponsor"
    )

    panels = [
        FieldPanel("logo"),
        FieldPanel("logo_alt"),
        FieldPanel("logo_en"),
        FieldPanel("logo_alt_en"),
    ]


class Social(Orderable):
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    page = ParentalKey(
        "GlobalSettings", on_delete=models.CASCADE, related_name="social"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
    ]


@register_setting
class GlobalSettings(BaseSetting, ClusterableModel):
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

    search = models.ForeignKey(
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

    brand_color = models.CharField(max_length=30, null=True, blank=True)
    text_color = models.CharField(max_length=30, null=True, blank=True)

    surface_color_one = models.CharField(max_length=30, null=True, blank=True)
    surface_color_two = models.CharField(max_length=30, null=True, blank=True)

    intern_website = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    design_panels = [
        MultiFieldPanel(
            [
                FieldPanel("logo"),
                FieldPanel("logo_title"),
            ],
            heading="Logo",
            classname="collapsible",
        ),
        MultiFieldPanel(
            [
                FieldPanel("brand_color"),
                FieldPanel("text_color"),
                FieldPanel("surface_color_one"),
                FieldPanel("surface_color_two"),
            ],
            heading="Brand Farben",
        ),
    ]

    contact_panels = [
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
        InlinePanel("social", label="Social Media"),
        InlinePanel("sponsor", label="Sponsoren"),
    ]

    link_panels = [
        MultiFieldPanel(
            [
                FieldPanel("contact"),
                FieldPanel("impressum"),
                FieldPanel("data_protection"),
                FieldPanel("search"),
            ],
            heading="Service",
        ),
        FieldPanel("intern_website"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(design_panels, heading="Design"),
            ObjectList(contact_panels, heading="Kontakte"),
            ObjectList(link_panels, heading="Links"),
        ]
    )

    class Meta:
        verbose_name = "Konfiguration"
