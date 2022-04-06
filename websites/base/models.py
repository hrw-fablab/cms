from wagtail.core.models import Orderable
from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from wagtail.core.fields import StreamField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
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

from websites.base.blocks import HomeBlock, FlexBlock, ProjectBlock


class HomePage(AbstractHomePage):
    template = "pages/home.html"
    body = StreamField(HomeBlock(), blank=True)

    content_panels = AbstractHomePage.content_panels + [
        StreamFieldPanel("body"),
    ]


class FolderPage(AbstractFolderPage):
    parent_page_types = ["HomePage"]
    subpage_type = ["FlexPage", "IndexPage"]


class FlexPage(AbstractFlexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = []

    template = "pages/flex.html"

    body = StreamField(FlexBlock(), blank=True)

    content_panels = AbstractHomePage.content_panels + [
        StreamFieldPanel("body"),
    ]


class ArticlePage(AbstractArticlePage):
    parent_page_types = ["IndexPage"]
    subpage_type = []

    template = "pages/article.html"


class IndexPage(AbstractIndexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = ["ArticlePage"]

    template = "pages/index.html"


class IndexCategoryPage(AbstractIndexPage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["DevicePage", "ProjectPage"]

    template = "pages/category.html"

    def get_context(self, request):
        context = super().get_context(request)
        all_children = self.get_children().live().specific()
        context["children"] = all_children
        return context

    class Meta:
        verbose_name = "Index Seite mit Kategorien"


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

    parent_page_types = ["IndexCategoryPage"]
    subpage_type = []

    body = StreamField(ProjectBlock(), blank=True)

    content_panels = AbstractProjectPage.content_panels + [
        InlinePanel("project_links", label="Project Links"),
        StreamFieldPanel("body"),
    ]


class DevicePage(AbstractDevicePage):
    template = "pages/project.html"

    parent_page_types = ["IndexCategoryPage"]
    subpage_type = []

    body = StreamField(ProjectBlock(), blank=True)

    content_panels = AbstractDevicePage.content_panels + [
        StreamFieldPanel("body"),
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


class EventsPage(AbstractBasePage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = []

    template = "pages/category.html"

    class Meta:
        verbose_name = "Events Auflistung"