from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from wagtail.search.backends import get_search_backend

from home.models import BlogPage, AboutPageQuestion


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    backend = get_search_backend()

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query).results()

        query = Query.get(search_query)

        search_results += backend.search(search_query, AboutPageQuestion.objects.all()).results()

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 20)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
