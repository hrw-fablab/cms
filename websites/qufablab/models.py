from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from abstract.pages.home import AbstractHomePage
from abstract.pages.folder import AbstractFolderPage
from abstract.pages.flex import AbstractFlexPage
from abstract.pages.index import AbstractIndexPage
from abstract.pages.article import AbstractArticlePage
from abstract.pages.search import AbstractSearchPage

from websites.base.blocks import HomeBlock, FlexBlock

from django.db import models
from wagtail.core.models import Page


class HomePage(AbstractHomePage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    template = "pages/home.html"

    body = StreamField(HomeBlock(), blank=True)

    content_panels = AbstractHomePage.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "QuFabLab Startseite"


class FolderPage(AbstractFolderPage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    parent_page_types = ["HomePage"]
    subpage_type = ["FlexPage", "IndexPage"]


class FlexPage(AbstractFlexPage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = []

    template = "pages/flex.html"

    body = StreamField(FlexBlock(), blank=True)

    content_panels = AbstractHomePage.content_panels + [
        StreamFieldPanel("body"),
    ]


class ArticlePage(AbstractArticlePage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    parent_page_types = ["IndexPage"]
    subpage_type = []

    template = "pages/article.html"


class IndexPage(AbstractIndexPage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    childrenPage = ArticlePage

    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = ["ArticlePage"]

    template = "pages/index.html"


class SearchPage(AbstractSearchPage):
    page_ptr = models.OneToOneField(
        Page,
        auto_created=True,
        parent_link=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/search.html"
