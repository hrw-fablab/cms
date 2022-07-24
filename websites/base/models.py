from wagtail.models import Orderable
from django.db import models

from wagtail.admin.panels import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import StreamField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from abstract.pages.device import AbstractDevicePage

from abstract.pages.home import AbstractHomePage
from abstract.pages.folder import AbstractFolderPage
from abstract.pages.flex import AbstractFlexPage
from abstract.pages.index import AbstractIndexPage
from abstract.pages.article import AbstractArticlePage
from abstract.pages.search import AbstractSearchPage
from abstract.pages.project import AbstractProjectPage
from abstract.pages.base import AbstractBasePage

from abstract.models.links import Link, ExpireLink, PageLink
from forms.models import FabLabCaptchaEmailForm

from websites.base.blocks import (
    HomeBlock,
    FlexBlock,
    ProjectBlock,
    DeviceBlock,
    FormBlock,
)

from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class HomePage(AbstractHomePage):
    subpage_type = [
        "FolderPgae",
        "FlexPage",
        "IndexPage",
        "DeviceIndexPage",
        "ProjectIndexPage",
        "SearchPage",
        "CollectionPage",
        "FormPage",
    ]

    template = "pages/flex.html"
    body = StreamField(HomeBlock(), blank=True, use_json_field=True)

    content_panels = AbstractHomePage.content_panels + [
        FieldPanel("body"),
    ]


class FolderPage(AbstractFolderPage):
    parent_page_types = ["HomePage"]
    subpage_type = ["FlexPage", "IndexPage", "DeviceIndexPage", "ProjectIndexPage"]


class FlexPage(AbstractFlexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = []

    template = "pages/flex.html"

    body = StreamField(FlexBlock(), blank=True, use_json_field=True)

    content_panels = AbstractHomePage.content_panels + [
        FieldPanel("body"),
    ]


class ArticlePage(AbstractArticlePage):
    parent_page_types = ["IndexPage"]
    subpage_type = []

    template = "pages/article.html"


class IndexPage(AbstractIndexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = ["ArticlePage"]

    template = "pages/index.html"


class DeviceIndexPage(AbstractIndexPage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["DevicePage"]

    template = "pages/category.html"

    def get_context(self, request):
        context = super().get_context(request)
        all_children = self.get_children().live().specific()
        context["children"] = all_children
        return context

    class Meta:
        verbose_name = "Geräte"


class ProjectIndexPage(AbstractIndexPage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ProjectPage"]

    template = "pages/category.html"

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            self.get_children().live().specific().order_by("-projectpage__category")
        )
        context["children"] = all_children
        return context

    class Meta:
        verbose_name = "Projekte"


class SearchPage(AbstractSearchPage):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/search.html"


class ProjectPageLink(Orderable, Link):
    page = ParentalKey(
        "ProjectPage", on_delete=models.CASCADE, related_name="project_links"
    )


class ProjectPage(AbstractProjectPage):
    template = "pages/project.html"

    parent_page_types = ["ProjectIndexPage"]
    subpage_type = []

    body = StreamField(ProjectBlock(), blank=True, use_json_field=True)

    content_panels = AbstractProjectPage.content_panels + [
        InlinePanel("project_links", label="Project Links"),
        FieldPanel("body"),
    ]


class DevicePage(AbstractDevicePage):
    template = "pages/project.html"

    parent_page_types = ["DeviceIndexPage"]
    subpage_type = []

    body = StreamField(DeviceBlock(), blank=True, use_json_field=True)

    content_panels = AbstractDevicePage.content_panels + [
        FieldPanel("body"),
    ]


class CollectionPagePage(Orderable, PageLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_pages"
    )


class CollectionPageLink(Orderable, ExpireLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_links"
    )


class CollectionPage(AbstractBasePage, ClusterableModel):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/collection.html"

    content_panels = AbstractBasePage.content_panels + [
        InlinePanel("collection_links", label="Link", classname="collabsible"),
        InlinePanel("collection_pages", label="Page", classname="collabsible"),
    ]

    class Meta:
        verbose_name = "Link Sammlung"


from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
    FORM_FIELD_CHOICES,
)


class FormField(AbstractFormField):
    CHOICES = FORM_FIELD_CHOICES + (("pageParam", "Page Parameter"),)

    page = ParentalKey("FormPage", related_name="form_fields")
    field_type = models.CharField(
        verbose_name="field type",
        max_length=16,
        choices=CHOICES,
    )


class FormPage(FabLabCaptchaEmailForm):
    parent_page_types = ["HomePage", "FolderPage", "FlexPage"]
    subpage_type = []

    body = RichTextField(
        blank=True,
        features=[
            "bold",
            "italic",
            "link",
            "document-link",
        ],
    )

    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("body"),
        InlinePanel("form_fields", label="Form Elemente"),
        FieldPanel("thank_you_text", heading="Bestätigung"),
        MultiFieldPanel(
            [
                FieldPanel("from_address"),
                FieldPanel("to_address"),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    template = "forms/form_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context["params"] = request.GET
        return context

    class Meta:
        verbose_name = "Form Seite"
