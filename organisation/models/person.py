from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    MultiFieldPanel,
    FieldPanel,
    TabbedInterface,
    ObjectList,
)


class Person(ClusterableModel):
    title = models.CharField("First Name", max_length=100, null=True, blank=True)
    first_name = models.CharField("First Name", max_length=254)
    last_name = models.CharField("Last Name", max_length=254)

    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    organisation = models.ForeignKey(
        "organisation.Organisation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    link = models.URLField(max_length=254, null=True, blank=True)
    responsibility = models.CharField(max_length=254, null=True, blank=True)

    en_responsibility = models.CharField(max_length=254, null=True, blank=True)

    german = [
        MultiFieldPanel(
            [
                FieldPanel("title", heading="Titel"),
                FieldPanel("first_name", heading="Vornahme"),
                FieldPanel("last_name", heading="Nachnahme"),
            ],
            heading="Name",
        ),
        FieldPanel("organisation", heading="Organisation"),
        FieldPanel("image", heading="Bild"),
        MultiFieldPanel(
            [
                FieldPanel("link", heading="Link"),
                FieldPanel("responsibility", heading="Aufgabenbereiche"),
            ],
            heading="Informationen",
        ),
    ]

    english = [
        MultiFieldPanel(
            [
                FieldPanel("en_responsibility", heading="Aufgabenbereiche"),
            ],
            heading="Information",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(german, heading="Deutsch"),
            ObjectList(english, heading="English"),
        ]
    )

    @property
    def name(self):
        if self.title:
            return "{} {}".format(self.title, self.first_name)
        else:
            return "{}".format(self.first_name)

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition("fill-70x70").img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ""

    def __str__(self):
        if self.title:
            return "{} {} {}".format(self.title, self.first_name, self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personen"
