from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

def search(request):
    local_query = request.GET.get('local', None)
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    if local_query == "en":
        filter_local = 2
    elif local_query == "de":
        filter_local = 1
    else:
        filter_local = 1


    # Search
    if search_query:
        search_results = Page.objects.live().filter(locale = filter_local).specific().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    return TemplateResponse(request, 'pages/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
