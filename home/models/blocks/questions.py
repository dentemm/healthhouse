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

class QuestionsEmbedBlock(EmbedBlock):

  class Meta:
    template = 'home/questions/blocks/embed.html'
    icon = 'media'
    label = 'Video embed'

class CustomRichTextBlock(RichTextBlock):

  class Meta:
    template = 'home/questions/blocks/richtext.html'
    label = 'Richtext'

class QuestionAnswerBlock(StructBlock):

  question = CharBlock(max_length=300)
  question_asker = CharBlock(max_length=64, required=False)
  answer = TextBlock(max_length=512)
  answerer = CharBlock(max_length=128, required=False)

  class Meta:
    template = 'home/questions/blocks/question_answer.html'
    icon = 'help'
    label = 'Question + Answer'

class QuestionsPageStreamBlock(StreamBlock):

  subtitle = SubtitleBlock()
  paragraph = ParagraphBlock()
  image = ImageWithCaptionblock()
  gallery = CarouselBlock(child_block=ImageWithCaptionblock)
  richtext = CustomRichTextBlock()
  question_answer = QuestionAnswerBlock()
  video_embed = QuestionsEmbedBlock()
    