from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from abstract.pages.index import AbstractIndexPage
from ..models.article import ArticlePage

from wagtail.core.models import Page

class IndexPage(AbstractIndexPage):
    template = "pages/index.html"

    childrenPage = ArticlePage

    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ArticlePage"]
