import geopy
import ssl
from datetime import datetime, date, time

from django.db import models

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.api import APIField

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from .helpers import Address, GeneralBullet
from ..variables import PARTNER_CHOICES, TEAM_MEMBER_CHOICES, TRANSPORTATION_CHOICES

@register_snippet
class Location(Address, index.Indexed):

    name = models.CharField(verbose_name='location name', max_length=64)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    
    class Meta:
		    verbose_name = 'location'
		    verbose_name_plural = 'locations'
		    ordering = ['name', ]
        
    def __str__(self):
		    return self.name
        
    @property
    def to_string(self):
		    return '%s %s %s' % (self.street, self.number, self.city)
        
    def save(self, *args, **kwargs):

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        geopy.geocoders.options.default_ssl_context = ctx

        geolocator = geopy.geocoders.Nominatim()
            
        address_string = self.street + ' ' + self.number + ' ' + self.postal_code + ' ' + self.city + ' ' + str(self.country.name)

        loc = geolocator.geocode(address_string)
        
        if not isinstance(loc, geopy.location.Location):

            alternative = self.street + ' ' + self.postal_code + ' ' + self.city + ' ' + str(self.country.name)
            loc = geolocator.geocode(alternative)
            
        if isinstance(loc, geopy.location.Location):

            self.latitude = loc.latitude
            self.longitude = loc.longitude
            
        return super(Location, self).save(*args, **kwargs)

Location.panels = [
	  MultiFieldPanel([
			  FieldRowPanel([
					  FieldPanel('name', classname='col6'),
				    ]	
			  ),
			  FieldRowPanel([
					  FieldPanel('street', classname='col8'),
					  FieldPanel('number', classname='col4')
          ]),
        FieldRowPanel([
            FieldPanel('city', classname='col8'),
            FieldPanel('postal_code', classname='col4')
        ]),
        FieldRowPanel([
            FieldPanel('country', classname='col6'),
        ]),
    ], heading='Location details')
]

@register_snippet
class Partner(index.Indexed, models.Model):

    name = models.CharField(max_length=128)
    url = models.URLField(verbose_name='Website', blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    logo_white = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    partner_type = models.IntegerField(choices=PARTNER_CHOICES, null=True)
    recent_visitor = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partners & visitors'
        verbose_name_plural = 'Partners & visitors'

Partner.panels = [
  	MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('name', classname='col6'),
                FieldPanel('partner_type', classname='col6')
            ]),
            FieldRowPanel([
                ImageChooserPanel('logo', classname='col6'),
                ImageChooserPanel('logo_white', classname='col6'),
                FieldPanel('url', classname='col6')
                
            ]),
            FieldRowPanel([
                FieldPanel('description', classname='col8'),
                FieldPanel('recent_visitor', classname='col4')               
            ])
		], 
        heading='Partner informatation'
	)  
]

Partner.search_field = [
    index.SearchField('name', partial_match=True)
]

@register_snippet
class TeamMember(Orderable):

    name = models.CharField(max_length=64)
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=64)
    bio = models.TextField(null=True)
    user_type = models.IntegerField(verbose_name='Type', choices=TEAM_MEMBER_CHOICES)
    picture = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team members'
        ordering = ['sort_order']

TeamMember.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('name', classname='col6'),
            FieldPanel('user_type', classname='col6'),
            FieldPanel('email', classname='col6')
        ]),
        FieldPanel('title'),
        ImageChooserPanel('picture'),
        FieldPanel('bio')
    ], heading='Team member')
]

@register_snippet
class InterestingNumber(ClusterableModel, models.Model):

    number = models.IntegerField()
    identifier = models.CharField(verbose_name='label', max_length=28)

    def __str__(self):
        return '%d %s' % (self.number, self.identifier)

InterestingNumber.panels = [
    MultiFieldPanel([
        FieldRowPanel(
            [
                FieldPanel('number', classname='col4'),
                FieldPanel('identifier', classname='col4')
            ]
        )
    ], heading='Interesting number'),
    InlinePanel('bullets', label='Bullets')
]

@register_snippet
class Storyline(ClusterableModel, models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )
    company = models.ForeignKey(
        Partner,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']

Storyline.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image'),
        SnippetChooserPanel('company')
    ], heading='Storyline'),
    InlinePanel('bullets', label='Extra information (bullet list)')
]

class StorylineBullet(GeneralBullet):

    expo_area = ParentalKey(Storyline, on_delete=models.CASCADE, related_name='bullets', null=True)

@register_snippet
class ExpoArea(ClusterableModel, models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering=['id']

ExpoArea.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Exhibition area'),
    InlinePanel('bullets', label='Extra information (bullet list)')
]

class ExpoAreaBullet(GeneralBullet):

    expo_area = ParentalKey(ExpoArea, on_delete=models.CASCADE, related_name='bullets', null=True)

@register_snippet
class MeetingRoom(ClusterableModel, models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering=['id']

MeetingRoom.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Meeting room'),
    InlinePanel('bullets', label='Extra information (bullet list)')
]

class MeetingRoomBullet(GeneralBullet):

    expo_area = ParentalKey(MeetingRoom, on_delete=models.CASCADE, related_name='bullets', null=True)

@register_snippet
class Project(ClusterableModel, models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )
    link_title = models.CharField(max_length=24, null=True)
    link = models.URLField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']

Project.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('link_title', classname='col6'),
            FieldPanel('link', classname='col6'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Project information'),
    InlinePanel('bullets', label='Extra information (bullet list)')
]

class ProjectBullet(GeneralBullet):

    project = ParentalKey(Project, on_delete=models.CASCADE, related_name='bullets', null=True)

@register_snippet
class Testimonial(models.Model):

    quote = models.CharField(max_length=255)
    name = models.CharField(max_length=32)
    visible = models.BooleanField(default=True)
    company = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name + ': "' + self.quote + '"'

Testimonial.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('quote', classname='col9')
        ]),
        FieldRowPanel([
            FieldPanel('name', classname='col6'),
            FieldPanel('visible', classname='col6')
        ]),
        FieldRowPanel([
            FieldPanel('company', classname='col6')
        ])
    ], heading='Testimonial')
]

@register_snippet
class PressArticle(models.Model):

    title = models.CharField(max_length=64)
    description = models.TextField(max_length=300)

    link = models.URLField(blank=True, null=True)
    link_title = models.CharField(max_length=32, blank=True, null=True)

    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    document_link_title = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.title

PressArticle.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
            FieldPanel('description', classname='col8'),
            FieldPanel('link', classname='col6'),
            FieldPanel('link_title', classname='col6'),
            DocumentChooserPanel('document', classname='col6'),
            FieldPanel('document_link_title', classname='col6')
        ]),
    ],
    heading='Press article'
    )
]

@register_snippet
class Directions(ClusterableModel, models.Model):

    transportation_means = models.CharField(choices=TRANSPORTATION_CHOICES, max_length=32)

    def __str__(self):
        return self.transportation_means

    class Meta:
        verbose_name = 'directions'
        verbose_name_plural = 'directions'

Directions.panels = [
    MultiFieldPanel([
        FieldRowPanel(
            [
                FieldPanel('transportation_means', classname='col6'),
            ]
        )
    ], heading='Directions'),
    InlinePanel('bullets', label='Bullets')
]

class DirectionsBullets(GeneralBullet):

    directions = ParentalKey(Directions, on_delete=models.CASCADE, related_name='bullets', null=True)

class CalendarItem(models.Model):

    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField(default=date.today)
    start = models.TimeField(default=time(9, 00))
    end = models.TimeField(default=time(10, 00))
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+',
      blank=True
    )

    def __str__(self):
        return self.title

CalendarItem.api_fields = [
    APIField('title'),
    APIField('description'),
    APIField('date')
]

@register_snippet
class PublicEvent(CalendarItem):

    max_attendees = models.IntegerField(default=0, blank=False)
    price = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.title

PublicEvent.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('description', classname='col8')
        ]),
        FieldRowPanel([
            FieldPanel('price', classname='col6'),
            FieldPanel('max_attendees', classname='col6')
        ]),
        FieldRowPanel([
            FieldPanel('date', classname='col6')
        ]),
        FieldRowPanel([
            FieldPanel('start', classname='col6'),
            FieldPanel('end', classname='col6')         
        ]),
        ImageChooserPanel('image')
    ], heading='Public Event')
]