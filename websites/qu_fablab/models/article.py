from wagtail.core.models import Page
from abstract.pages.article import AbstractArticlePage


class QuArticlePage(AbstractArticlePage):
    parent_page_types = ["QuIndexPage"]
    subpage_type = []

    template = "pages/article.html"

    def get_context(self, request):
        context = super().get_context(request)
        parent = Page.get_parent(self)
        context["parent"] = parent
        return context

    class Meta:
        verbose_name = "Artikel Seite"
