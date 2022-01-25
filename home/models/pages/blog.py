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

from ..snippets import PressArticle
from ..blocks import BlogPageStreamBlock

class BlogIndexPage(Page):

  introduction = models.TextField(null=True)
  press_title = models.CharField(max_length=32, null=True)
  press_text = models.CharField(max_length=255, null=True)

  template = 'home/blog_index_page.html'

  def blogs(self): 
    return BlogPage.objects.live().order_by('-first_published_at')

  def press_articles(self):
    return PressArticle.objects.all().order_by('-id')

BlogIndexPage.content_panels = Page.content_panels + [
  FieldPanel('introduction'),
  MultiFieldPanel([
    FieldPanel('press_title'),
    FieldPanel('press_text')
  ], heading='Press', classname='collapsible collapsed')
]

BlogIndexPage.parent_page_types = ['home.HomePage']
BlogIndexPage.subpage_types = ['home.BlogPage']

class BlogpageTag(TaggedItemBase):

  content_object = ParentalKey('home.BlogPage', on_delete=models.CASCADE, related_name='tagged_blogs')

class BlogPage(Page):

  intro = models.TextField(null=True)
  cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
  content = StreamField(BlogPageStreamBlock(), null=True)

  tags = ClusterTaggableManager(through=BlogpageTag, blank=True)

  template = 'home/blog_article_page.html'
  
  def latest_articles(self):
    return BlogPage.objects.live().sibling_of(self, inclusive=False).order_by('-first_published_at')[0:3]

  def get_context(self, request):
    context = super().get_context(request)
    context['other_articles'] = self.latest_articles()
    context['previous'] = request.META.get('HTTP_REFERER')

    return context

BlogPage.content_panels = [
  MultiFieldPanel([
    FieldPanel('title'),
    FieldPanel('intro'),
    ImageChooserPanel('cover_image'),
  ], heading='Title & intro'),
  MultiFieldPanel([
    StreamFieldPanel('content')
  ], heading='Content'),
  MultiFieldPanel([
    FieldPanel('tags')
  ], heading='Tags')
]

BlogPage.search_fields = Page.search_fields + [
  index.SearchField('intro'),
  index.SearchField('tags')
]

BlogPage.parent_page_types = ['home.BlogIndexPage']
BlogPage.subpage_types = []