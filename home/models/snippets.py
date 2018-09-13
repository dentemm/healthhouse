import geopy
import ssl

from django.db import models

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from modelcluster.models import ClusterableModel

from .helpers import Address
from ..variables import PARTNER_CHOICES, TEAM_MEMBER_CHOICES

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
    url = models.URLField(verbose_name='Website')
    description = models.TextField(null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
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
            FieldPanel('user_type', classname='col6')
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
class Storyline(models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )

    def __str__(self):
        return self.title

Storyline.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Storyline')
]

@register_snippet
class ExpoArea(models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )

    def __str__(self):
        return self.title

ExpoArea.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Exhibition area')
]

@register_snippet
class MeetingRoom(models.Model):

    title = models.CharField(max_length=155, null=True, blank=False)
    text = models.TextField(null=True)
    image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.CASCADE,
      related_name='+'
    )

    def __str__(self):
        return self.title

MeetingRoom.panels = [
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('title', classname='col8'),
        ]),
        FieldRowPanel([
            FieldPanel('text', classname='col9')
        ]),
        ImageChooserPanel('image')
    ], heading='Meeting room')
]