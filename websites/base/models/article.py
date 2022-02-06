from wagtail.core.models import Page
from abstract.pages.article import AbstractArticlePage


class ArticlePage(AbstractArticlePage):
    parent_page_types = ["IndexPage"]
    subpage_type = []

    template = "pages/article.html"
