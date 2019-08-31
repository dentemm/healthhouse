from datetime import date

from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from ..snippets import Event
from ...forms.private_event_form import EventVisitorForm

class EventListPage(Page):

    introduction = models.TextField(null=True)

    template = 'home/events/agenda_page.html'

    def events(self):
        return Event.objects.all() \
                    .filter(date__gte=date.today()) \
                    .filter(is_private=False) \
                    .order_by('date')

EventListPage.content_panels = [

    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('introduction')
    ],
    heading='General information'
    )
]

EventListPage.subpage_types = []

class PrivateEventListPage(Page):

    template = 'home/events/agenda_page.html'

    def events(self):
        return Event.objects.all() \
                    .filter(date__gte=date.today()) \
                    .filter(is_private=True) \
                    .order_by('date')

PrivateEventListPage.content_panels = [

    MultiFieldPanel([
        FieldPanel('title'),
    ],
    heading='General information'
    )
]

PrivateEventListPage.subpage_types = [
    'home.PrivateEventPage',
]

class PrivateEventPage(Page):

    template = 'home/events/private_event.html'

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def serve(self, request):

        if request.method == 'POST':

            form = EventVisitorForm(request.POST)

            if form.is_valid():

                # form.cleaned_data['event_id'] = self.event.pk

                print('form is valid')
                print(form)

                visitor = form.save(commit=False)

                visitor.event_id = self.event.pk

                visitor.save()

                print(visitor)

            print('dit werkt!')
            return super(PrivateEventPage, self).serve(request)

        return super(PrivateEventPage, self).serve(request)

    def get_context(self, request):

        ctx = super(PrivateEventPage, self).get_context(request)

        print('get context')

        if request.method == 'POST':

            form = EventVisitorForm(request.POST)

            ctx['form'] = form

            print('get context - POST')
            return ctx

        form = EventVisitorForm()
        ctx['form'] = form

        return ctx

PrivateEventPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        SnippetChooserPanel('event')
    ])
]

PrivateEventPage.subpage_types = []
PrivateEventPage.parent_page_types = [
   PrivateEventListPage
]