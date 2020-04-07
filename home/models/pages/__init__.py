from datetime import date

from django.db import models
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.contrib import messages

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase, Tag

from wagtailcaptcha.models import WagtailCaptchaForm

from .events import EventListPage, PrivateEventListPage
from ..blocks import HomePageStreamBlock, BlogPageStreamBlock, DiscoveryPageStreamBlock
from ..snippets import InterestingNumber, Partner, TeamMember, Location, Storyline, ExpoArea, MeetingRoom, Project, Testimonial, PressArticle, Directions, Event
from ...variables import SOCIAL_MEDIA_CHOICES, ICON_CHOICES, DISCOVERY_PAGE_CHOICES

#
# WAGTAIL SETTINGS
#
@register_setting
class HealthHouseSettings(ClusterableModel, BaseSetting):

    tagline = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=28, null=True)
    email = models.EmailField(null=True)
    vat_number = models.CharField(verbose_name='VAT / BTW', max_length=16, null=True)
    account = models.CharField(verbose_name='Account number', max_length=24, null=True)

    logo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    logo_minimal = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    logo_white = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
        )

    error_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Health House data'

HealthHouseSettings.panels = [
    MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('vat_number', classname='col6'),
                FieldPanel('account', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('email', classname='col6'),
                FieldPanel('phone_number', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('location', classname='col6')
            ])
        ], 
        heading='General information'
    ),
    MultiFieldPanel([
        ImageChooserPanel('logo'),
        ImageChooserPanel('logo_minimal'),
        ImageChooserPanel('logo_white')
    ], 
        heading='Logos',
        classname='collapsible collapsed'
    ),
    FieldPanel('tagline'),
    MultiFieldPanel([
        InlinePanel('related_links', label='External links')
    ],
        heading='External links',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        ImageChooserPanel('error_image')
    ],
        heading='Error pages',
        classname='collapsible collapsed'
    )
]

#
# HELPERS
#
class LinkFields(models.Model):

	link_external = models.URLField('External link', blank=True)
	link_page = models.ForeignKey(
		'wagtailcore.Page',
        verbose_name='Link to page',
        on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='+'
	)

	class Meta:
		abstract = True

LinkFields.panels = [
	FieldPanel('link_external'),
    FieldPanel('link_page')
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
	MultiFieldPanel([
        FieldPanel('link_external'),
    ], heading='Link'),
]    

class HealthHouseRelatedLink(Orderable, RelatedLink):

	page = ParentalKey(
        'home.HealthHouseSettings',
        related_name='related_links',
        null=True,
        on_delete=models.SET_NULL
        )

#
# PAGES
#

class HomePage(Page):

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
        verbose_name='Link1',
		null=True,
		blank=True,
		related_name='+',
        on_delete=models.SET_NULL
	)
    discover_link_alternative = models.URLField(verbose_name='Link1 - Alternative', null=True, blank=True)
    discover_link_text = models.CharField(verbose_name='Link text', max_length=32, null=True)
    discover_link2 = models.ForeignKey(
		'wagtailcore.Page',
        verbose_name='Link2',
		null=True,
		blank=True,
		related_name='+',
        on_delete=models.SET_NULL
	)
    discover_link2_alternative = models.URLField(verbose_name='Link2 - Alternative', null=True, blank=True)
    discover_link2_text = models.CharField(verbose_name='Link2 text', max_length=32, null=True)

    visit_title = models.CharField(
        max_length=63,
        null=True
    )
    visit_text = models.CharField(
        max_length=255,
        null=True,
        )

    newsletter_title = models.CharField(
        max_length=64,
        null=True
    )
    newsletter_info = models.CharField(
        max_length=255,
        null=True
    )

    feature_title = models.CharField(
        verbose_name='title',
        max_length=63,
        null=True
    )

    number_title = models.CharField(
        verbose_name='title',
        max_length=63,
        null=True
    )
    number_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def latest_articles(self): 
        return BlogPage.objects.live().order_by('-first_published_at')[0:4]

    def upcoming_events(self):
        # return Event.objects.all()
        return Event.objects.all() \
            .exclude(event_type=2) \
            .filter(date__gte=date.today()) \
            .order_by('date')[0:4]

    def discover_link_1(self):
        
        if self.discover_link:
            return self.discover_link.url
        
        elif self.discover_link_alternative:
            return self.discover_link_alternative

    def discover_link_2(self):

        if self.discover_link2:
            return self.discover_link2.url
        
        elif self.discover_link2_alternative:
            return self.discover_link2_alternative

    def numbers(self):
        return InterestingNumber.objects.all()[0:3]

    def testimonials(self):
        return Testimonial.objects.all().filter(visible=True)

    def recent_visitors(self):
        return Partner.objects.all().filter(recent_visitor=True)

    def get_context(self, request):

        context = super().get_context(request)
        context['latest_articles'] = self.latest_articles
        
        return context

HomePage.content_panels = Page.content_panels + [
    MultiFieldPanel(
        [
            ImageChooserPanel('logo')
        ],
        heading='General information',
        classname='collapsible'
    ),
    MultiFieldPanel(
        [
            InlinePanel('cover_images', label=_('Cover images')),
        ],
        heading='Cover images',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('discover_title'),
            FieldPanel('discover_text'),
            FieldRowPanel([
                PageChooserPanel('discover_link'),
                FieldPanel('discover_link_alternative', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('discover_link_text', classname='col6')
            ]),
            FieldRowPanel([
                PageChooserPanel('discover_link2'),
                FieldPanel('discover_link2_alternative', classname='col6')
            ]),
            FieldRowPanel([
                FieldPanel('discover_link2_text', classname='col6')
            ]),

        ],
        heading='Discover HH',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('feature_title'),
            InlinePanel(
                'features',
                label='Core values',
                min_num=3,
                max_num=3
                ),
        ],
        heading='Core values',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            InlinePanel(
                'masonry_images',
                label='Masonry images',
                help_text='Currently designed to hold 8 images',
                min_num=8,
                max_num=8
            )
        ],
        heading='Masonry images (designed for 8 images)',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('newsletter_title'),
            FieldPanel('newsletter_info')
        ],
        heading='Newsletter',
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            FieldPanel('number_title'),
            ImageChooserPanel('number_image'),
        ],
        heading='Interesting numbers',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            FieldPanel('visit_title'),
            FieldPanel('visit_text'),
        ],
        heading='Recent visits',
        classname='collapsible collapsed'
    ),  
]

HomePage.parent_page_types = []
HomePage.subpage_types = [
    'home.ContactPage',
    'home.DiscoveryPage',
    'home.AboutPage',
    'home.BlogIndexPage',
    'home.PartnerPage',
    EventListPage,
    PrivateEventListPage,
    'home.PrivacyPage',
    'home.CoronaIndexPage'
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
        ordering = ['sort_order']

HomePageCoverImage.panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption')
]

class HomePageFeatures(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(verbose_name='Core value', max_length=128)
    text = models.CharField(verbose_name='Description', max_length=255)
    icon = models.CharField(verbose_name='Icon', max_length=40, choices=ICON_CHOICES, null=True)

    link_title = models.CharField(max_length=24, null=True)
    link = models.ForeignKey(
		'wagtailcore.Page',
        verbose_name='Link',
		null=True,
		blank=True,
		related_name='+',
        on_delete=models.SET_NULL
	)

    class Meta:
        verbose_name = 'Core value'
        verbose_name_plural = 'Core values'
        ordering = ['sort_order']

HomePageFeatures.panels = [

    FieldRowPanel([
        FieldPanel('title', classname='col6'),
        FieldPanel('icon', classname='col6')
    ]),
    FieldPanel('text'),
    FieldPanel('link_title'),
    PageChooserPanel('link')
]

class HomePageMasonry(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='masonry_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

HomePageMasonry.panels = [
    ImageChooserPanel('image')
]

class Bullet(Orderable, models.Model):

    bullet = models.CharField(max_length=64)
    number = ParentalKey('home.InterestingNumber', on_delete=models.CASCADE, related_name='bullets', null=True)

    def __str__(self):
        return self.bullet

    class Meta:
        ordering = ['sort_order']

Bullet.panels = [
    FieldPanel('bullet')
]

class ContactPage(WagtailCaptchaForm, AbstractEmailForm):

    directions_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def directions(self):
        return Directions.objects.all()

    thank_you_text = models.CharField(default='Thank you for your message!', max_length=160)

    template = 'home/contact_page.html'

    def save(self, *args, **kwargs):

        if not self.from_address:
            self.from_address = 'info@health-house.be'

        super(ContactPage, self).save(*args, **kwargs)

    def serve(self, request, *args, **kwargs):

        ctx = self.get_context(request)

        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
            
            if form.is_valid():
                self.process_form_submission(form)
                ctx['form'] = self.get_form(page=self, user=request.user)
                messages.success(request, self.thank_you_text)
                return render(request, self.get_landing_page_template(request), ctx)

            else: 
                ctx['form'] = form
                return render(request, self.get_landing_page_template(request), ctx)

        form = self.get_form(page=self, user=request.user)                
        ctx['form'] = form 

        return render(request, self.get_template(request), ctx)

    def get_landing_page_template(self, request, *args, **kwargs):
        return self.template

    def send_mail(self, form):

        subject = self.subject
        receivers = [self.to_address, ]
        sender = self.from_address

        ctx = {}
        ctx['form'] = form
        content = get_template('home/mails/contact_form.html').render(ctx)
        
        msg = EmailMessage(subject, content, to=receivers, from_email=sender)
        msg.content_subtype = 'html'
        msg.send()

    class Meta:
        verbose_name = 'Contact page'
        verbose_name_plural = 'Contact pages'

ContactPage.content_panels = Page.content_panels + [
    ImageChooserPanel('directions_image'),
    MultiFieldPanel(
        [
            FieldPanel('subject'),
            FieldPanel('thank_you_text'),
            FieldRowPanel([
                FieldPanel('to_address', classname='col6'),
                FieldPanel('from_address', classname='col6')
            ])
        ],
        heading='Form configuration',
        classname='collapsible collapsed'
    ),
    MultiFieldPanel(
        [
            InlinePanel('form_fields', label='Form fields'),
        ],
        heading='Form fields',
        classname='collapsible collapsed'
    )
]

ContactPage.parent_page_types = ['home.HomePage']
ContactPage.subpage_types = []

class ContactPageFormField(AbstractFormField):
    page = ParentalKey(ContactPage, related_name='form_fields')

class DiscoveryPage(Page):

    introduction = models.TextField()
    content = StreamField(DiscoveryPageStreamBlock(), null=True)
    
DiscoveryPage.content_panels = Page.content_panels + [

    FieldPanel('introduction'),
    MultiFieldPanel([
        StreamFieldPanel('content')
    ], heading='Content')
]

DiscoveryPage.parent_page_types = ['home.HomePage']
DiscoveryPage.subpage_types = ['home.DiscoveryDetailPage']

class DiscoveryDetailPage(Page):

    introduction = models.TextField(null=True)
    discover_detail = models.CharField(verbose_name='Page type', max_length=28, choices=DISCOVERY_PAGE_CHOICES, null=True)

    template = 'home/discovery_detail_page.html'

    def content(self):

        if (self.discover_detail == 'storylines'):
            return Storyline.objects.all()

        elif (self.discover_detail == 'meeting_rooms'):
            return MeetingRoom.objects.all()

        elif (self.discover_detail == 'expo_rooms'):
            return ExpoArea.objects.all()

        elif (self.discover_detail == 'projects'):
            return Project.objects.all()

        return []

DiscoveryDetailPage.content_panels = Page.content_panels + [
    FieldPanel('introduction'),
    FieldPanel('discover_detail')
]

DiscoveryDetailPage.parent_page_types = ['home.DiscoveryPage']
DiscoveryDetailPage.subpage_types = []

class AboutPage(Page):

    description = models.TextField(null=True)

    def core_team_members(self):
        return TeamMember.objects.filter(user_type=1)

    def board_members(self):
        return TeamMember.objects.filter(user_type=2)

    def brand_ambassadors(self):
        return TeamMember.objects.filter(user_type=3)

AboutPage.content_panels = Page.content_panels + [
    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('description')
    ], heading='General information'),
    MultiFieldPanel([
        InlinePanel('topics', label='Topics (mission, vision, ...)')
    ],
    heading='Topics (mission, vision, ...)',
    classname='collapsible collapsed'
    ),
    MultiFieldPanel([
        InlinePanel('faq_questions', label=_('FAQ questions'))
    ],
    heading='FAQ questions',
    classname='collapsible collapsed' 
    )
]

AboutPage.parent_page_types = ['home.HomePage']
AboutPage.subpage_types = []

AboutPage.search_fields = Page.search_fields + [
    index.SearchField('description')
]

class AboutPageQuestion(index.Indexed, Orderable):

    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='faq_questions')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ question'
        verbose_name_plural = 'FAQ questions'
        ordering = ['sort_order']

AboutPageQuestion.panels = [
    MultiFieldPanel([
        FieldPanel('question'),
        FieldPanel('answer')
    ])
]

# AboutPageQuestion.search_fields = [
#     index.SearchField('question'),
#     index.SearchField('answer')
# ]

class AboutPageTopic(Orderable):

    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(verbose_name='Name', max_length=28)
    description = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topic: (mission, vision, ...)'
        verbose_name_plural = 'Topics'

AboutPageTopic.panels = [
    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('description')
    ])
]

AboutPageTopic.search_fields = [
    index.SearchField('title'),
    index.SearchField('description')
]
 
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
    ],
    heading='Press',
    classname='collapsible collapsed'
    )
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

class CoronaIndexPage(Page):

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

CoronaIndexPage.content_panels = Page.content_panels + [
    # FieldPanel('introduction'),
    # MultiFieldPanel([
    #     FieldPanel('press_title'),
    #     FieldPanel('press_text')
    # ],
    # heading='Press',
    # classname='collapsible collapsed'
    # )
]

CoronaIndexPage.parent_page_types = ['home.HomePage']
CoronaIndexPage.subpage_types = ['home.CoronaArticlePage']


class CoronaArticlePageTag(TaggedItemBase):

    content_object = ParentalKey('home.CoronaArticlePage', on_delete=models.CASCADE, related_name='tagged_corona_articles')

class CoronaArticlePage(Page):

    cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    tags = ClusterTaggableManager(through=CoronaArticlePageTag, blank=True)

    template = 'home/corona/corona_detail_page.html'

    # related articles
    related_title = models.CharField(verbose_name='Title related art.', max_length=64, default='Related articles')

    def get_tags(self):
        tags = self.tags.all()

        return tags

    def previous_url(self):
        return self.request.META.get('HTTP_REFERER')

    def related_articles(self):

        all_articles = CoronaArticlePage.objects.all()

        if all_articles.count <= 4:
            return all_articles

        if self.tags.length == 0:
            return all_articles

            

        # else:



        # for tag in self.tags:
        #     print(tag)



CoronaArticlePage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title'),
        ImageChooserPanel('cover_image'),
    ], heading='Title & intro'),
    # MultiFieldPanel([
    #     StreamFieldPanel('content')
    # ], heading='Content'),
    MultiFieldPanel([
        FieldPanel('related_title')
    ], heading='Related articles'),
    MultiFieldPanel([
        FieldPanel('tags')
    ], heading='Tags')
]

CoronaArticlePage.search_fields = Page.search_fields + [
    # index.SearchField('intro'),
    index.SearchField('tags')
]

CoronaArticlePage.parent_page_types = ['home.CoronaIndexPage']
CoronaArticlePage.subpage_types = []


class PartnerPage(Page):

    introduction = models.TextField(null=True)
    visible = models.BooleanField(default=True)

    founding_title = models.CharField(max_length=28, null=True)
    founding_text = models.CharField(max_length=155, null=True)

    structural_title = models.CharField(max_length=28, null=True)
    structural_text = models.CharField(max_length=155, null=True)

    trusted_title = models.CharField(max_length=28, null=True)
    trusted_text = models.CharField(max_length=155, null=True)

    def founding_partners(self):
        return Partner.objects.filter(partner_type=1)

    def structural_partners(self):
        return Partner.objects.filter(partner_type=2)

    def trusted_members(self):
        return Partner.objects.filter(partner_type=5)

PartnerPage.content_panels = [

    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('introduction')
    ],
        heading='General information'
    ),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('founding_title', classname='col7'),
            FieldPanel('founding_text', classname='col7')
        ])
    ],
        heading='Founding partners'
    ),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('structural_title', classname='col7'),
            FieldPanel('structural_text', classname='col7')
        ])
    ],
        heading='Structural partners'
    ),
    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('trusted_title', classname='col7'),
            FieldPanel('trusted_text', classname='col7')
        ])
    ],
        heading='Trusted members'
    )
]

PartnerPage.parent_page_types = ['home.HomePage']
PartnerPage.subpage_types = []

class PrivacyPage(Page):

    policy = RichTextField()

    template = 'home/privacy_policy.html'

PrivacyPage.content_panels = [

    MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('policy')
    ],
    heading='General information'
    )
]

PrivacyPage.parent_page_types = ['home.HomePage']
PrivacyPage.subpage_types = []