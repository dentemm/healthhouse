from wagtail.core.blocks import StreamBlock, StructBlock, CharBlock, ListBlock, TextBlock, RichTextBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock

from .variables import COLOR_CHOICES, IMAGE_POSITION_CHOICES

class ImageWithCaptionblock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'

class CarouselBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/owl_carousel.html'
        icon = 'image'

class ParallaxBlock(StructBlock):

    image = ImageChooserBlock()
    background_color = ChoiceBlock(choices=COLOR_CHOICES)
    image_position = ChoiceBlock(choices=IMAGE_POSITION_CHOICES)
    
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
    rich_text = CustomRichTextBlock()