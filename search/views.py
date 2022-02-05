from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)


    # Search
    if search_query:
        search_results = Page.objects.live().specific().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    return TemplateResponse(request, 'pages/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
