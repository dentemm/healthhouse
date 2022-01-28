from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
  MultiFieldPanel,
  StreamFieldPanel,
  FieldPanel,
)

from ..blocks.questions import QuestionsPageStreamBlock

class QuestionsOverview(Page):

  template = 'home/questions/questions_overview.html'

  info_text = models.TextField(verbose_name='description', null=True)
  
  # last
  def featured(self):
    return QuestionsPage.objects.all() \
      .order_by('-first_published_at')[0]

  # All but last
  def others(self):

    if QuestionsPage.objects.count() > 1:
      return QuestionsPage.objects.all() \
        .order_by('-first_published_at')[:-1]

    return None

  def get_context(self, request):
    context = super().get_context(request)
    context['previous'] = request.META.get('HTTP_REFERER')
    return context

QuestionsOverview.content_panels = Page.content_panels + [
  FieldPanel('info_text')
]

QuestionsOverview.parent_page_types = ['home.HomePage']
QuestionsOverview.subpage_types = ['home.QuestionsPage']

class QuestionsPage(Page):

  template = 'home/questions/questions_page.html'

  content = StreamField(QuestionsPageStreamBlock(), null=True)
  
  cover_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=True
  )

QuestionsPage.content_panels = Page.content_panels + [
  MultiFieldPanel([
    StreamFieldPanel('content')
  ], heading='Content')
]

QuestionsPage.parent_page_types = ['home.QuestionsOverview']
QuestionsPage.subpage_types = []