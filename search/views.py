from wagtail.models import Page
from wagtail.search.models import Query
from django.http import JsonResponse

import json

def search_json(request):
    search_query = request.GET.get("query", None)

    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        query.add_hit()
    
    search_json = []

    for element in search_results:
        search_json.append({
            "title": element.title
        })
    return JsonResponse(search_json, safe=False)
