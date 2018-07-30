import geopy

from django.db import models
from django.utils.translation import ugettext as _

from wagtail.core.models import Page, Orderable
from wagtail.core.blocks import StreamBlock, StructBlock, CharBlock, ListBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from modelcluster.fields import ParentalKey

from django_countries.fields import CountryField

#
# STREAMFIELD DEFINITIONS
#

class ImageWithCaptionblock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        icon='image'

class CarouselBlock(ListBlock):
    items = ImageWithCaptionblock()

class HomePageStreamBlock(StreamBlock):
    test = ImageWithCaptionblock(label='testje', icon='image')
    test2 = ListBlock(ImageWithCaptionblock(), label='Image slider', min=3)

#
# PAGES
#

class HomePage(Page):
    body = StreamField(HomePageStreamBlock(), null=True)

HomePage.content_panels = Page.content_panels + [
    # StreamFieldPanel('body'),
    InlinePanel('cover_images', label=_('Cover images'))
]

class HomePageCoverImage(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='cover_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=55)

    class Meta:
        verbose_name = 'Cover image'
        verbose_name_plural = 'Cover images'

HomePageCoverImage.panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption')
]


class ContactPage(Page):

    pass

class DiscoveryPage(Page):

    introduction = models.TextField()
    
DiscoveryPage.content_panels = Page.content_panels + [

    FieldPanel('introduction')
]

class AboutPage(Page):

    pass 

AboutPage.content_panels = Page.content_panels + [
    InlinePanel('faq_questions', label=_('FAQ questions'))
]

class BlogIndexPage(Page):
    
    def get_context(self, request):

        context = super().get_context(request)
        blogs = self.get_children().live().order_by('-first_published_at')
        context['blogs'] = blogs
        
        return context

BlogIndexPage.content_panels = Page.content_panels + [
    
]

class BlogPage(Page):
    
    intro = models.TextField(null=True)
    # TEMM: need to remove null=True below
    cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
    
    date = models.DateField(_('Date'))


BlogPage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('intro'),
        ImageChooserPanel('cover_image'),
    ], heading='Title & intro'),
    FieldPanel('date'),
    InlinePanel('gallery_images', label=_('Gallery images'))
]

class BlogPageGallery(Orderable):

    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=160)

    class Meta:
        verbose_name = 'Gallery image'
        verbose_name_plural = 'Gallery images'

BlogPageGallery.panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption')
]

#
# SNIPPETS
#
@register_snippet
class Address(models.Model):

    city = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=8)
    street = models.CharField(max_length=40)
    number = models.CharField(max_length=8)
    country = CountryField(null=True, default='BE')

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        ordering = ['city', ]
        
    def __str__(self):
        return '%s - %s' % (self.city, self.street)

Address.panels = [
	MultiFieldPanel([
			FieldRowPanel([
					FieldPanel('street', classname='col8'),
					FieldPanel('number', classname='col4')
				]
			),
			FieldRowPanel([
					FieldPanel('city', classname='col8'),
					FieldPanel('postal_code', classname='col4')
				]
			),
			FieldRowPanel([
					FieldPanel('country', classname='col6'),
				]
			),
		], heading='Address details'
	),
]

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

	def save(self, *args, **kwargs):

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
				]
			),
			FieldRowPanel([
					FieldPanel('city', classname='col8'),
					FieldPanel('postal_code', classname='col4')
				]
			),
			FieldRowPanel([
					FieldPanel('country', classname='col6'),
				]
			),
		],
		heading='Location details'
	)
]

@register_snippet
class Partner(models.Model):

    name = models.CharField(max_length=128)
    url = models.URLField(verbose_name='Website url')
    description = models.TextField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

Partner.panels = [
  	MultiFieldPanel([
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('description'),
        ImageChooserPanel('logo')
		], 
        heading='Location details'
	)  
]

class AboutPageQuestion(Orderable):

    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='faq_questions')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ question'
        verbose_name_plural = 'FAQ questions'

AboutPageQuestion.panels = [
    MultiFieldPanel([
        FieldPanel('question'),
        FieldPanel('answer')
    ])
]