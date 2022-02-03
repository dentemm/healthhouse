from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
  MultiFieldPanel,
  StreamFieldPanel,
  FieldPanel,
  InlinePanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from ..blocks.questions import QuestionsPageStreamBlock

class QuestionsOverviewCategory(models.Model):

  page = ParentalKey('home.QuestionsOverview', on_delete=models.CASCADE, related_name='categories')

  name = models.CharField(max_length=164)
  description = models.TextField()

QuestionsOverviewCategory.panels = [
  FieldPanel('name', classname='col12'),
  FieldPanel('description', classname='col12')
]

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
  FieldPanel('info_text'),
  MultiFieldPanel([
    InlinePanel('categories')
  ], heading='Categories')
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
    ImageChooserPanel('cover_imgage')
  ]),
  MultiFieldPanel([
    StreamFieldPanel('content')
  ], heading='Content')
]

QuestionsPage.parent_page_types = ['home.QuestionsOverview']
QuestionsPage.subpage_types = []