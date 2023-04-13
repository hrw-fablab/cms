from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Site
from wagtail.documents.models import Document, AbstractDocument
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtailmedia.models import AbstractMedia

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtailcache.cache import WagtailCacheMixin

OGTYPECHOICES = (
    ("website", "website"),
    ("article", "article"),
    ("profile", "profile"),
)

TWTYPECHOICES = (
    ("summary_large_image", "summary_large_image"),
    ("summary", "summary"),
    ("player", "player"),
)

INDEXCHOICES = (
    ("index", "index"),
    ("noindex", "noindex"),
)


# Custom Image Model
# https://docs.wagtail.io/en/stable/advanced_topics/images/custom_image_model.html
class FablabImage(AbstractImage):
    credit = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + ("credit",)


# Allows Custom Image to Use Renditions
class FablabRendition(AbstractRendition):
    image = models.ForeignKey(
        "FablabImage", on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


# Custom Document Model
# https://docs.wagtail.io/en/stable/advanced_topics/documents/custom_document_model.html
class FablabDocument(AbstractDocument):
    credit = models.CharField(max_length=255, blank=True)

    admin_form_fields = Document.admin_form_fields + ("credit",)


# Custom Media Model
# https://github.com/torchbox/wagtailmedia
class FablabMedia(AbstractMedia):
    preview = models.ForeignKey(
        FablabImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    advanced_mobile = models.FileField(
        upload_to="media", verbose_name=_("file"), blank=True
    )

    admin_form_fields = (
        "title",
        "file",
        "collection",
        "preview",
        "tags",
        "advanced_mobile",
    )


# Abstract Base Page Layout
class FablabBasePage(WagtailCacheMixin, Page):
    index = models.CharField(max_length=255, choices=INDEXCHOICES, default="index")

    og_image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    og_image_alt = models.CharField(max_length=255, null=True, blank=True)

    og_type = models.CharField(max_length=255, choices=OGTYPECHOICES, default="website")

    tw_size = models.CharField(
        max_length=255, choices=TWTYPECHOICES, default="summary_large_image"
    )

    promote_panels = Page.promote_panels + [
        FieldPanel("index", heading="Index"),
        MultiFieldPanel(
            [
                FieldPanel("og_image", heading="Image"),
                FieldPanel("og_image_alt", heading="Image alt text"),
                FieldPanel("og_type", heading="Page Type"),
            ],
            heading="Open Graph",
        ),
        MultiFieldPanel(
            [
                FieldPanel("tw_size", heading="Image Size"),
            ],
            heading="Twitter",
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["menuitems"] = (
            Site.find_for_request(request)
            .root_page.get_children()
            .live()
            .public()
            .in_menu()
        )
        return context

    class Meta:
        abstract = True
