from wagtail.core.blocks import (
  CharBlock,
  ListBlock,
  TextBlock,
  StructBlock,
  StreamBlock,
  RichTextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class ParagraphBlock(TextBlock):

  class Meta:
    template = 'home/questions/blocks/paragraph.html'
    icon = 'edit'
    label = 'Paragraph'

class SubtitleBlock(CharBlock):

  class Meta:
    template = 'home/questions/blocks/subtitle.html'
    icon = 'title'
    label = 'Subtitle'

class ImageWithCaptionblock(StructBlock):
  image = ImageChooserBlock()
  caption = CharBlock(required=False)

  class Meta:
    template = 'home/questions/blocks/image.html'
    icon = 'image'
    label = 'Single Image'

class CarouselBlock(ListBlock):

  class Meta:
    template = 'home/questions/blocks/gallery.html'
    icon = 'image'
    label = 'Gallery'

class EmbedBlock(EmbedBlock):

  class Meta:
    template = 'home/questions/blocks/embed.html'
    icon = 'media'
    label = 'Video embed'

class CustomRichTextBlock(RichTextBlock):

  class Meta:
    template = 'home/questions/blocks/rich_text.html'
    label = 'Richtext'

class QuestionsPageStreamBlock(StreamBlock):

    paragraph = ParagraphBlock()
    gallery = CarouselBlock(child_block=ImageWithCaptionblock)
    richtext = CustomRichTextBlock()