from wagtail.models import Page
from wagtail.search.models import Query
from django.http import JsonResponse


def search_json(request):
    search_query = request.GET.get("query", None)

    if search_query:
        search_results = Page.objects.live().filter(locale_id=1).search(search_query)
        query = Query.get(search_query)

        query.add_hit()

    search_json = []

    for element in search_results:
        search_json.append({"title": element.title, "url": element.url})
    return JsonResponse(search_json[0:5], safe=False)
