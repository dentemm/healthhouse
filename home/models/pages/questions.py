from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

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
    return QuestionsPage.objects.all() \
      .order_by('-first_published_at')[:-1]

QuestionsOverview.content_panels = Page.content_panels + [

]

QuestionsOverview.parent_page_types = ['home.HomePage']
QuestionsOverview.subpage_types = ['home.QuestionsPage']

class QuestionsPage(Page):

  content = StreamField(QuestionsPageStreamBlock(), null=True)
  
  cover_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=True
  )

QuestionsPage.content_panels = Page.content_panels + []