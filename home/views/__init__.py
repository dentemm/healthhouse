import csv

from ..models.pages import HomePage

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

def mailchimp(request):

    try:
        mailchimp = MailchimpMarketing.Client()
        mailchimp.set_config({
            'api_key': 'fbad732a46ab8b211a1bb0ae680f61c8-us13',
            'server': 'us13'
        })

        list_id = "9bb5a9f1da"
        email_address = request.POST.get('email_address')

        print('-------')
        print(email_address)

        member_info = {
            "email_address": email_address,
            "status": "pending",
            "merge_fields": {
                "FNAME": "",
                "LNAME": ""
                }
            }

        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))

        message = "Your e-mail address was successfully added to our mailing list, please check your inbox for a confirmation e-mail!"

        response = JsonResponse({"result": {
            "success": message
            }
        })

        return response

    except ApiClientError as error:

        print("An exception occurred: {}".format(error.text))

        message = "This e-mail address could not be added to our mailing list ..."

        response = JsonResponse({"result": {
            "error": message
            }
        })
        return response

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