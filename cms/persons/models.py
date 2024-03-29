from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel

from wagtail.search import index


class Person(index.Indexed, ClusterableModel):
    personal_title = models.CharField("Title", max_length=100, null=True, blank=True)
    first_name = models.CharField("First Name", max_length=254)
    last_name = models.CharField("Last Name", max_length=254)

    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    link = models.URLField(max_length=254, null=True, blank=True)
    responsibility = models.CharField(max_length=254, null=True, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("personal_title", heading="Titel"),
                FieldRowPanel(
                    [
                        FieldPanel("first_name", heading="Vorname"),
                        FieldPanel("last_name", heading="Nachname"),
                    ]
                ),
            ],
            heading="Name",
        ),
        FieldPanel("image", heading="Bild"),
        MultiFieldPanel(
            [
                FieldPanel("link", heading="Link"),
                FieldPanel("responsibility", heading="Aufgabenbereiche"),
            ],
            heading="Informationen",
        ),
    ]

    search_fields = [
        index.AutocompleteField("first_name"),
        index.AutocompleteField("last_name"),
    ]

    @property
    def name(self):
        if self.personal_title:
            return "{} {} {}".format(
                self.personal_title, self.first_name, self.last_name
            )
        else:
            return "{} {}".format(self.first_name, self.last_name)

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition("fill-70x70").img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ""

    thumb_image.fget.short_description = "Bild"

    def __str__(self):
        if self.personal_title:
            return "{} {} {}".format(
                self.personal_title, self.first_name, self.last_name
            )
        else:
            return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personen"
