from datetime import date

from django.db import models
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import get_template

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from ..snippets import Event
from ..helpers.events import EventVisitor
from ...forms.private_event_form import EventVisitorForm

class EventListPage(Page):

    introduction = models.TextField(null=True)

    template = 'home/events/agenda_page.html'

    def events(self):
        return Event.objects.all() \
                    .filter(date__gte=date.today()) \
                    .exclude(event_type=2) \
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

    template = 'home/events/private_agenda.html'

    def events(self):
        return PrivateEventPage.objects.all().order_by('event__date')

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

class PrivateEventVisitorPage(Page):

    template = 'home/events/visitor_overview.html'

    def event(self):
        return self.get_parent().specific.event

    def serve(self, request):

        if request.method == 'POST':

            if (request.user and request.user.is_authenticated):
                form = request.POST

                try:
                    pk = form.get('userid')
                    visitor = EventVisitor.objects.get(pk=pk)
                    visitor.delete()

                    return super(PrivateEventVisitorPage, self).serve(request)

                except:
                    return super(PrivateEventVisitorPage, self).serve(request)

                return super(PrivateEventVisitorPage, self).serve(request)

            else: 
                pass

        return super(PrivateEventVisitorPage, self).serve(request)

class PrivateEventPage(Page):

    template = 'home/events/private_event.html'

    event_information = models.TextField('Introduction text', null=True)
    question_text = models.TextField(verbose_name='Contact information', null=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def serve(self, request):

        if self.get_descendants().count() == 0:
            self.add_child(instance=PrivateEventVisitorPage(title='visitors', slug='visitors', live=True))

        if request.method == 'POST':

            form = EventVisitorForm(request.POST)

            if form.is_valid() and self.get_remaining() > 0:
                visitor = form.save(commit=False)
                visitor.event_id = self.event.pk

                self.send_email(visitor)
                visitor.save()

            return super(PrivateEventPage, self).serve(request)

        return super(PrivateEventPage, self).serve(request)

    def get_context(self, request):

        ctx = super(PrivateEventPage, self).get_context(request)
        ctx['remaining_places'] = self.get_remaining()

        if request.method == 'POST':

            form = EventVisitorForm(request.POST)
            if form.is_valid():

                form = EventVisitorForm()
                ctx['form'] = form
                messages.success(request, 'Thank you for subscribing, see you at the event!')
                return ctx

            ctx['form'] = form
            return ctx

        form = EventVisitorForm()
        ctx['form'] = form

        return ctx
    
    def get_remaining(self):

        remaining = self.event.max_attendees - self.event.visitors.count()
        return remaining if remaining > 0 else 0

    def send_email(self, visitor):

        subject = 'Subscription to private event: ' + self.event.title
        receivers = ['events@health-house.be', ]
        sender = 'events@health-house.be'

        ctx = {}
        ctx['visitor'] = visitor
        ctx['event'] = self.event
        ctx['remaining'] = self.get_remaining() - 1
        content = get_template('home/mails/private_event_subscription.html').render(ctx)
        
        msg = EmailMessage(subject, content, to=receivers, from_email=sender)
        msg.content_subtype = 'html'
        msg.send()

PrivateEventPage.content_panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col6')
        ]),
        FieldRowPanel([
            FieldPanel('event_information', classname='col8'),
            FieldPanel('question_text', classname='col8')
        ])
    ], heading='General information'),
    MultiFieldPanel([
        SnippetChooserPanel('event')
    ], heading='Choose event')
]

PrivateEventPage.subpage_types = []
PrivateEventPage.parent_page_types = [
   PrivateEventListPage
]

PrivateEventVisitorPage.parent_page_types = [
    PrivateEventPage
]
PrivateEventVisitorPage.subpage_types = []