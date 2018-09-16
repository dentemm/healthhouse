from wagtail.core.blocks import (
    StreamBlock,
    StructBlock,
    CharBlock,
    ListBlock,
    TextBlock,
    RichTextBlock,
    ChoiceBlock,
    PageChooserBlock,
    URLBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

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

class ListItemBlock(StructBlock):

    item = CharBlock(max_length=255)

class CustomListBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/list.html'
        icon = 'list-ul'

class CustomURLBlock(StructBlock):

    url = URLBlock(required=False)
    title = CharBlock(max_length=28, required=False)

class ParallaxBlock(StructBlock):

    image = ImageChooserBlock()
    title = CharBlock(max_length=64)
    info_text = CharBlock(max_length=255)

    links = ListBlock(PageChooserBlock(), required=False)
    external_links = ListBlock(CustomURLBlock(), required=False)
    
    class Meta:
        template = 'home/partials/blocks/parallax.html'
        icon = 'code'

class QuoteBlock(StructBlock):
    quote = CharBlock(max_length=255)
    author = CharBlock(max_length=64)

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
    unordered_list = CustomListBlock(child_block=ListItemBlock)
    image = ImageWithCaptionblock()
    rich_text = CustomRichTextBlock()
    embed = CustomEmbedBlock()

class DiscoveryPageStreamBlock(StreamBlock):

    parallax = ParallaxBlock()
