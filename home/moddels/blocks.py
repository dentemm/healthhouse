from wagtail.core.blocks import (
    StreamBlock,
    StructBlock,
    CharBlock,
    ListBlock,
    TextBlock,
    RichTextBlock,
    ChoiceBlock,
    PageChooserBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from ..variables import COLOR_CHOICES, IMAGE_POSITION_CHOICES

class ImageWithCaptionblock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        template = 'home/partials/blocks/image_caption.html'
        icon = 'image'

class CustomEmbedBlock(EmbedBlock):

    class Meta:
        template = 'home/partials/blocks/embed.html'
        icon = 'media'

class CarouselBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/owl_carousel.html'
        icon = 'image'

class ParallaxBlock(StructBlock):

    image = ImageChooserBlock()
    title = CharBlock(max_length=64)
    info_text = CharBlock(max_length=255)
    background_color = ChoiceBlock(choices=COLOR_CHOICES)
    image_position = ChoiceBlock(choices=IMAGE_POSITION_CHOICES)

    links = ListBlock(PageChooserBlock())
    
    class Meta:
        template = 'home/partials/blocks/parallax.html'
        icon = 'code'

class QuoteBlock(StructBlock):
    quote = CharBlock(max_length='255')
    author = CharBlock(max_length='64')

    class Meta:
        template = 'home/partials/blocks/quote.html'
        icon = 'openquote'

class ParagraphBlock(TextBlock):

    class Meta:
        template = 'home/partials/blocks/paragraph.html'
        icon = 'edit'

class SubtitleBlock(CharBlock):

    class Meta:
        template = 'home/partials/blocks/subtitle.html'
        icon = 'title'

class CustomRichTextBlock(RichTextBlock):

    class Meta:
        template = 'home/partials/blocks/rich_text.html'

class HomePageStreamBlock(StreamBlock):

    test = ImageWithCaptionblock(label='testje', icon='image')
    images = ListBlock(ImageWithCaptionblock(), label='Image slider', min=3)

class BlogPageStreamBlock(StreamBlock):

    subtitle = SubtitleBlock()
    quote = QuoteBlock()
    paragraph = ParagraphBlock()
    gallery = CarouselBlock(child_block=ImageWithCaptionblock)
    image = ImageWithCaptionblock()
    rich_text = CustomRichTextBlock()
    embed = CustomEmbedBlock()

class DiscoveryPageStreamBlock(StreamBlock):

    parallax = ParallaxBlock()
