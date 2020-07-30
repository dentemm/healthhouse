from wagtail.core.blocks import (
    EmailBlock,
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
        label = 'Single Image'

class CoronaImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        template = 'home/corona/blocks/single_image.html'
        icon = 'image'
        label = 'Single Image'

class GifImageBlock(StructBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'home/corona/blocks/gif.html'
        icon = 'image'
        label = 'Gif image'

class CustomEmbedBlock(EmbedBlock):

    class Meta:
        template = 'home/partials/blocks/embed.html'
        icon = 'media'
        label = 'Video Embed'

class CoronaEmbedBlock(EmbedBlock):

    class Meta:
        template = 'home/corona/blocks/embed.html'
        icon = 'media'
        label = 'Video embed'

class CarouselBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/owl_carousel.html'
        icon = 'image'

class CoronaCarouselBlock(ListBlock):

    class Meta:
        template = 'home/corona/blocks/owl_carousel.html'
        icon = 'image'

class ListItemBlock(StructBlock):

    item = CharBlock(max_length=255)

class CustomListBlock(ListBlock):

    class Meta:
        template = 'home/partials/blocks/list.html'
        icon = 'list-ul'
        label = 'List'

class CoronaListBlock(ListBlock):

    class Meta:
        template = 'home/corona/blocks/list.html'
        icon = 'list-ul'
        label = 'List'

class CustomURLBlock(StructBlock):

    url = URLBlock(required=False)
    title = CharBlock(max_length=28, required=False)

class CustomEmailLinkBlock(StructBlock):

    url = EmailBlock(required=False)
    title = CharBlock(max_length=28, required=False)

class ParallaxBlock(StructBlock):

    image = ImageChooserBlock()
    title = CharBlock(max_length=64)
    info_text = CharBlock(max_length=255)

    links = ListBlock(PageChooserBlock(), required=False)
    external_links = ListBlock(CustomURLBlock(), required=False)
    mail_links = ListBlock(CustomEmailLinkBlock(), required=False)
    
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

class CoronaParagraphBlock(TextBlock):

    class Meta:
        template = 'home/corona/blocks/paragraph.html'
        icon = 'edit'

class SubtitleBlock(CharBlock):

    class Meta:
        template = 'home/partials/blocks/subtitle.html'
        icon = 'title'

class CoronaSubtitleBlock(CharBlock):

    class Meta:
        template = 'home/corona/blocks/subtitle.html'
        icon = 'title'

class CustomRichTextBlock(RichTextBlock):

    class Meta:
        template = 'home/partials/blocks/rich_text.html'

class CoronaRichTextBlock(RichTextBlock):

    class Meta:
        template = 'home/corona/blocks/rich_text.html'

class HomePageStreamBlock(StreamBlock):

    test = ImageWithCaptionblock(label='testje', icon='image')
    images = ListBlock(ImageWithCaptionblock(), label='Image slider', min=3)

class ButtonLinkBlock(StructBlock):

    button_text = CharBlock(max_lenght=64, required=True)
    internal_link = ListBlock(PageChooserBlock(), required=False)
    external_link = URLBlock(required=False)

    class Meta:
        template = 'home/partials/blocks/buttonlink.html'
        icon = 'site'
        label = 'Button link'

class CoronaButtonLinkBlock(StructBlock):

    button_text = CharBlock(max_lenght=64, required=True)
    internal_link = ListBlock(PageChooserBlock(), required=False)
    external_link = URLBlock(required=False)

    class Meta:
        template = 'home/corona/blocks/buttonlink.html'
        icon = 'site'
        label = 'Button link'

class BlogPageStreamBlock(StreamBlock):

    subtitle = SubtitleBlock()
    quote = QuoteBlock()
    paragraph = ParagraphBlock()
    gallery = CarouselBlock(child_block=ImageWithCaptionblock)
    unordered_list = CustomListBlock(child_block=ListItemBlock)
    image = ImageWithCaptionblock()
    rich_text = CustomRichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])
    embed = CustomEmbedBlock()
    link = ButtonLinkBlock()

class DiscoveryPageStreamBlock(StreamBlock):

    parallax = ParallaxBlock()

class CoronaArticleStreamBlock(StreamBlock):

    subtitle = CoronaSubtitleBlock()
    paragraph = CoronaParagraphBlock()
    rich_text = CustomRichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])
    unordered_list = CoronaListBlock(child_block=ListItemBlock)
    link = CoronaButtonLinkBlock()

class CoronaSidebarStreamBlock(StreamBlock):

    image = CoronaImageBlock()
    gif_image = GifImageBlock()
    embed = CoronaEmbedBlock()
    gallery = CoronaCarouselBlock(child_block=CoronaImageBlock)
    
