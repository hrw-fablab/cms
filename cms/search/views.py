from wagtail.models import Page
from wagtail.search.models import Query
from django.shortcuts import render


def search(request):
    search_query = request.GET.get("query", None)

    search_results = []

    if search_query:
        search_results = Page.objects.live().filter(locale_id=1).search(search_query)
        query = Query.get(search_query)

        query.add_hit()

    return render(
        request, "search.html", context={"search_results": search_results[0:5]}
    )
