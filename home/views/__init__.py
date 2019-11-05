import csv

from django.shortcuts import render
from django.http import HttpResponse

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

def csvView(request, slug):

    page = Page.objects.get(slug=slug).specific
    visitors = page.event.visitors.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visitor_export.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(['last name', 'first name', 'company', 'phone', 'email'])

    for visitor in visitors:
        writer.writerow([visitor.last_name, visitor.first_name, visitor.company, visitor.phone, visitor.email])

    return response