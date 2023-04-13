from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from core.models import FablabBasePage

from wagtail.models import Page


class SearchPage(FablabBasePage):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/search.html"

    def get_context(self, request):
        context = super().get_context(request)
        search_query = request.GET.get("query", None)
        locale_query = request.GET.get("locale", None)

        if locale_query == "en":
            filter_local = 2
        else:
            filter_local = 1

        if search_query is None:
            return context

        search_results = (
            Page.objects.live()
            .filter(locale_id=filter_local)
            .specific()
            .public()
            .search(search_query)
        )

        paginator = Paginator(search_results, 10)
        page = request.GET.get("page", 1)
        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)

        context["results"] = search_results
        return context

    class Meta:
        verbose_name = "Suche"
