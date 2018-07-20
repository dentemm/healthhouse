from django.db import models
from django.utils.translation import ugettext as _

from wagtail.core.models import Page, Orderable
from wagtail.core.blocks import StreamBlock, StructBlock, CharBlock, ListBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey

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
    cover_image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True)
    
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
