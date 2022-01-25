from django.db import models

from wagtail.core.models import Page

class QuestionsOverview(Page):
  
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
  pass