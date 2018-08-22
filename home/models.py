import geopy
import ssl

from django.db import models
from django.utils.translation import ugettext as _

from wagtail.core.models import Page, Orderable
from wagtail.core.blocks import StreamBlock, StructBlock, CharBlock, ListBlock, TextBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from django_countries.fields import CountryField

from .variables import SOCIAL_MEDIA_CHOICES
#
# WAGTAIL SETTINGS
#
@register_setting
class HealthHouseSettings(ClusterableModel, BaseSetting):

    tagline = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=28, null=True)
    email = models.EmailField(null=True)
    location = models.ForeignKey(
        'home.Location',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
        )

    class Meta:
        verbose_name = 'Health House data'

HealthHouseSettings.panels = [
    MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('email', classname='col6'),
                FieldPanel('phone_number', classname='col6')
            ])
        ],
        heading='contact information'
    ),
    FieldPanel('tagline'),
    FieldPanel('location'),
    InlinePanel('related_links', label='Links')
]

#
# SNIPPETS
#
class LinkFields(models.Model):

	link_external = models.URLField('External link', blank=True)

	class Meta:
		abstract = True

LinkFields.panels = [
	FieldPanel('link_external'),
]

class RelatedLink(LinkFields):

	title = models.IntegerField(verbose_name='Link naar', choices=SOCIAL_MEDIA_CHOICES)
	icon = models.CharField(max_length=64, null=True, blank=True)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):

		name = ''

		if self.title == 1:
			name = 'facebook'
		elif self.title == 2:
			name = 'twitter'
		elif self.title == 3:
			name = 'linkedin'
		elif self.title == 4:
			name = 'youtube'
		elif self.title == 5:
			name = 'instagram'
		else:
			name = 'link'

		self.icon = name

		return super(RelatedLink, self).save(*args, **kwargs)

RelatedLink.panels = [
	FieldPanel('title'),
	MultiFieldPanel(LinkFields.panels, 'Link')
]

class HealthHouseRelatedLink(Orderable, RelatedLink):

	page = ParentalKey(
        'home.HealthHouseSettings',
        related_name='related_links',
        null=True,
        on_delete=models.SET_NULL
        )

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

    def __str__(self):
        return self.name

Partner.panels = [
  	MultiFieldPanel(
        [
            FieldPanel('name'),
            FieldPanel('url'),
            FieldPanel('description'),
            ImageChooserPanel('logo')
		], 
        heading='Location details'
	)  
]

#
# STREAMFIELD DEFINITIONS
#

class ImageWithCaptionblock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        icon='image'

class CarouselBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/owl_carousel.html'
        icon = 'image'

class HomePageStreamBlock(StreamBlock):
    test = ImageWithCaptionblock(label='testje', icon='image')
    images = ListBlock(ImageWithCaptionblock(), label='Image slider', min=3)

class QuoteBlock(StructBlock):
    quote = CharBlock(max_length='255')
    author = CharBlock(max_length='64')

    class Meta:
        template = 'home/partials/blocks/quote.html'
        icon='openquote'

class ParagraphBlock(TextBlock):

    class Meta:
        template = 'home/partials/blocks/paragraph.html'
        icon='edit'

class BlogPageStreamBlock(StreamBlock):
    quote = QuoteBlock()
    paragraph = ParagraphBlock()
    gallery = CarouselBlock(child_block=ImageWithCaptionblock)

#
# PAGES
#

class HomePage(Page):
    body = StreamField(HomePageStreamBlock(), null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    discover_title = models.CharField(
        max_length=63,
        null=True,
        )
    discover_text = models.CharField(
        max_length=255,
        null=True,
        )
    discover_link = models.ForeignKey(
		'wagtailcore.Page',
		null=True,
		blank=True,
		related_name='+',
        on_delete=models.SET_NULL
	)

    def latest_articles(self): 
        return BlogPage.objects.live().order_by('-first_published_at')[0:4]

    def get_context(self, request):

        context = super().get_context(request)
        context['latest_articles'] = self.latest_articles
        
        return context

HomePage.content_panels = Page.content_panels + [
    # StreamFieldPanel('body'),
    MultiFieldPanel(
        [
            ImageChooserPanel('logo')
        ],
        heading='General information',
        classname='collapsible'
    ),
    MultiFieldPanel(
        [
            FieldPanel('discover_title'),
            FieldPanel('discover_text'),
            FieldPanel('discover_link')
        ],
        heading='Discover HH',
        classname='collapsible'
    ),
    InlinePanel('cover_images', label=_('Cover images')),
]

HomePage.parent_page_types = []
HomePage.subpage_types = [
    'home.ContactPage',
    'home.DiscoveryPage',
    'home.AboutPage',
    'home.BlogIndexPage',
    'home.PartnerPage'
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

    directions_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    template = 'home/contact_page.html'

    class Meta:
        verbose_name = 'Contact page'
        verbose_name_plural = 'Contact pages'

ContactPage.content_panels = Page.content_panels + [
    ImageChooserPanel('directions_image')
]

ContactPage.parent_page_types = ['home.HomePage']
ContactPage.subpage_types = []

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

    def blogs(self): 
        return self.get_children().live().order_by('-first_published_at')
    
    def get_context(self, request):

        context = super().get_context(request)
        context['blogs'] = self.blogs
        
        return context

BlogIndexPage.content_panels = Page.content_panels + [
    
]

BlogIndexPage.parent_page_types = [
    'home.HomePage',
]

BlogIndexPage.subpage_types = [
    'home.BlogPage',
]

class BlogPage(Page):

    intro = models.TextField(null=True)
    # TEMM: need to remove null=True below
    cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    content = StreamField(BlogPageStreamBlock(), null=True)

    template = 'home/blog_article_page.html'
    
    def latest_articles(self):
        return BlogPage.objects.live().sibling_of(self, inclusive=False).order_by('-first_published_at')[0:2]
        # return self.get_siblings(False).live().order_by('-first_published_at')

    def get_context(self, request):

        context = super().get_context(request)
        context['other_articles'] = self.latest_articles()

        return context

BlogPage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('intro'),
        ImageChooserPanel('cover_image'),
    ], heading='Title & intro'),
    MultiFieldPanel([
        StreamFieldPanel('content')
    ], heading='Content')
]

BlogPage.parent_page_types = [
    'home.BlogIndexPage'
]

BlogPage.subpage_types = []

class PartnerPage(Page):

    introduction = models.TextField(null=True)
    visible = models.BooleanField(default=True)

    def partners(self): 
        return Partner.objects.all()
    
    def get_context(self, request):

        context = super().get_context(request)

        context['partners'] = self.partners
        
        return context

PartnerPage.content_panels = [

    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('introduction')
    ], heading='General information')
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