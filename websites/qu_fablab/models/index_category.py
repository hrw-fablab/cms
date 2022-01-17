from wagtail.core.models import Page
from abstract.pages.index import AbstractIndexPage


class QuIndexCategoryPage(AbstractIndexPage):
    template = "pages/category.html"

    parent_page_types = ["QuFolderPage", "QuHomePage"]
    subpage_type = ["QuDevicePage", "QuProjectPage"]

    def get_context(self, request):
        context = super().get_context(request)
        children = (
            Page.objects.live().public().child_of(self).order_by("-last_published_at")
        )
        context["children"] = children
        return context

    class Meta:
        verbose_name = "Index Seite mit Kategorien"
