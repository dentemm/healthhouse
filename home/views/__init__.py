from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query

def search(request):

    template = 'home.search.html'

    search_query = request.GET.get('query', None)

    if search_query:
        search_results = Page.objects.live().search(search_query)

        Query.get(search_query).add_hit()

    else:
        search_results = Page.objects.none()

    ctx = {}
    ctx['search_query'] = search_query
    ctx['search_results'] = search_results

    return render(request, template, ctx)
