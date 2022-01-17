from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from abstract.pages.index import AbstractIndexPage
from ..models.article import ArticlePage


class IndexPage(AbstractIndexPage):
    template = "pages/index.html"

    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ArticlePage"]

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            ArticlePage.objects.live()
            .public()
            .child_of(self)
            .order_by("-last_published_at")
        )
        if request.GET.get("author"):
            all_children = all_children.filter(
                author__last_name=request.GET.get("author")
            ).order_by("-last_published_at")

        paginator = Paginator(all_children, 4)
        page = request.GET.get("page")
        try:
            children = paginator.page(page)
        except PageNotAnInteger:
            children = paginator.page(1)
        except EmptyPage:
            children = paginator.page(paginator.num_pages)
        context["children"] = children

        if request.GET.get("tag"):
            children = (
                ArticlePage.objects.live()
                .public()
                .child_of(self)
                .filter(tag__name=request.GET.get("tag"))
                .order_by("-last_published_at")
            )
            context["children"] = children
        return context

    class Meta:
        verbose_name = "Index Seite"
