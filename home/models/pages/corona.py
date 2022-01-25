from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
  FieldPanel,
  StreamFieldPanel,
  MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from ..blocks import CoronaArticleStreamBlock, CoronaSidebarStreamBlock, CoronaFullWidthStreamBlock

class CoronaIndexPage(Page):

  intro = models.CharField('Introduction', max_length=512, default='Introduction text here ...')
  info_tags = models.CharField

  template = 'home/corona/corona_index_page.html'

  def articles(self): 
    return CoronaArticlePage.objects.live().order_by('-last_published_at')

  def all_tags(self):

    tags = []
    pages = CoronaArticlePage.objects.live()

    for page in pages:
      tags += page.get_tags()

    tags = sorted(set(tags))

    return tags

CoronaIndexPage.content_panels = [
  MultiFieldPanel([
    FieldPanel('title'),
    FieldPanel('intro')
  ], heading='General information')
]

CoronaIndexPage.parent_page_types = ['home.HomePage']
CoronaIndexPage.subpage_types = ['home.CoronaArticlePage']


class CoronaArticlePageTag(TaggedItemBase):
  content_object = ParentalKey('home.CoronaArticlePage', on_delete=models.CASCADE, related_name='tagged_corona_articles')

class CoronaArticlePage(Page):

  cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
  author = models.CharField('Author or resource', max_length=64, null=True, blank=True)

  content = StreamField(CoronaArticleStreamBlock(), null=True)
  sidebar = StreamField(CoronaSidebarStreamBlock(), null=True, blank=True)
  fullwidth = StreamField(CoronaFullWidthStreamBlock(), null=True, blank=True)

  tags = ClusterTaggableManager(through=CoronaArticlePageTag, blank=True)

  template = 'home/corona/corona_detail_page.html'

  # related articles
  related_title = models.CharField(verbose_name='Title related art.', max_length=64, default='Related articles')

  def get_context(self, request):
    context = super().get_context(request)
    context['previous'] = request.META.get('HTTP_REFERER')

    return context

  def get_tags(self):
      return self.tags.all()

  def related_articles(self):

    all_articles = CoronaArticlePage.objects.all()

    if all_articles.count <= 4:
      return all_articles

    if self.tags.length == 0:
      return all_articles

CoronaArticlePage.content_panels = [
  MultiFieldPanel([
    FieldPanel('title'),
    FieldPanel('author'),
    ImageChooserPanel('cover_image'),
  ], heading='Title & intro'),
  MultiFieldPanel([
    StreamFieldPanel('content')
  ], heading='Main content'),
  MultiFieldPanel([
    StreamFieldPanel('sidebar')
  ], heading='Sidebar content'),
  MultiFieldPanel([
    StreamFieldPanel('fullwidth')
  ], heading='Bottom fullwidth content'),
  MultiFieldPanel([
    FieldPanel('related_title')
  ], heading='Related articles'),
  MultiFieldPanel([
    FieldPanel('tags')
  ], heading='Tags')
]

CoronaArticlePage.search_fields = Page.search_fields + [
  index.SearchField('tags')
]

CoronaArticlePage.parent_page_types = ['home.CoronaIndexPage']
CoronaArticlePage.subpage_types = []
