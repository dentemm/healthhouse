from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
  FieldPanel,
  StreamFieldPanel,
  MultiFieldPanel,
  FieldRowPanel,
  InlinePanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from ..blocks.friends import FriendsPageStreamBlock
from ..helpers import GeneralBullet

class FriendsPagePlan(ClusterableModel, models.Model):

  page = ParentalKey('home.FriendsPage', on_delete=models.CASCADE, related_name='plans')

  name = models.CharField(max_length=64)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  description = models.TextField()

FriendsPagePlan.panels = [
  FieldPanel('name', classname='col12'),
  FieldPanel('price', classname='col12'),
  FieldPanel('description', classname='col12'),
  InlinePanel('bullets', label='Bullets', classname='col12')
]

class PlanBullet(GeneralBullet):
  plan = ParentalKey(FriendsPagePlan, on_delete=models.CASCADE, related_name='bullets', null=True)


class FriendsPage(Page):

  template = 'home/friends/friends_page.html'

  cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=False)
  
  content = StreamField(FriendsPageStreamBlock())

  contact_name = models.CharField(max_length=164)
  contact_title = models.CharField(max_length=164)
  contact_email = models.EmailField()
  contact_phone = models.CharField(max_length=24)

  contact_photo = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=False
  )

FriendsPage.content_panels = Page.content_panels + [
  MultiFieldPanel([
    ImageChooserPanel('cover_image', classname='col12'),
    StreamFieldPanel('content'),
  ], heading='Inhoud', classname='collapsible'),
  MultiFieldPanel([
    InlinePanel('plans', label='Plans', classname='col12')
  ], heading='Plans', classname='collapsible'),
  MultiFieldPanel([
    FieldRowPanel([
      ImageChooserPanel('contact_photo', classname='col6'),
      FieldPanel('contact_name', classname='col6'),
      FieldPanel('contact_title', classname='col6'),
      FieldPanel('contact_email', classname='col6'),
      FieldPanel('contact_phone', classname='col6'),
    ]),
  ], heading='Contact details', classname='collapsible'),
]

FriendsPage.parent_page_types = ['home.HomePage']
FriendsPage.subpage_types = []
