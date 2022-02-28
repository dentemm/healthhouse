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
from ...variables import QUESTION_CATEGORY_CHOICES

class QuestionsOverviewCategory(models.Model):

  page = ParentalKey('home.QuestionsOverview', on_delete=models.CASCADE, related_name='categories')

  name = models.CharField(max_length=164)
  description = models.TextField()
  hide = models.BooleanField(default=True)

QuestionsOverviewCategory.panels = [
  FieldPanel('name', classname='col12'),
  FieldPanel('description', classname='col12'),
  FieldPanel('hide', classname='col6')
]

class QuestionsOverview(Page):

  template = 'home/questions/questions_overview.html'

  cover_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=False
  )
  info_text = models.TextField(verbose_name='description', null=True)
  
  # last
  def featured(self):
    return QuestionsPage.objects.live() \
      .order_by('-first_published_at')[0]

  # All but last
  def others(self):

    count = QuestionsPage.objects.live().count()

    if count > 1:
      return QuestionsPage.objects.live() \
        .order_by('-first_published_at')[1:count]

    return None

  def get_context(self, request):
    context = super().get_context(request)
    context['previous'] = request.META.get('HTTP_REFERER')
    return context

QuestionsOverview.content_panels = Page.content_panels + [
  FieldPanel('info_text'),
  ImageChooserPanel('cover_image'),
  MultiFieldPanel([
    InlinePanel('categories')
  ], heading='Categories')
]

QuestionsOverview.parent_page_types = ['home.HomePage']
QuestionsOverview.subpage_types = ['home.QuestionsPage']

class QuestionsPage(Page):

  template = 'home/questions/questions_page.html'

  cover_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=True
  )
  category = models.IntegerField(choices=QUESTION_CATEGORY_CHOICES, default=1)
  content = StreamField(QuestionsPageStreamBlock(), null=True)

QuestionsPage.content_panels = Page.content_panels + [
  MultiFieldPanel([
    ImageChooserPanel('cover_image', classname='col12'),
    FieldPanel('category', classname='col12')
  ], heading='Info'),
  MultiFieldPanel([
    StreamFieldPanel('content')
  ], heading='Content')
]

QuestionsPage.parent_page_types = ['home.QuestionsOverview']
QuestionsPage.subpage_types = []