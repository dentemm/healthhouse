from wagtail.core.blocks import (
  CharBlock,
  StreamBlock,
  RichTextBlock,
  StructBlock,
  ListBlock,
  DecimalBlock,
)

class TitleBlock(CharBlock):

  class Meta:
    template = 'home/friends/blocks/title.html'
    icon = 'title'
    label = 'Title1'

class SubtitleBlock(CharBlock):

  class Meta:
    template = 'home/friends/blocks/subtitle.html'
    icon = 'title'
    label = 'Title2'

class PlanBlock(StructBlock):
  
    name = CharBlock(max_length=64)
    price = DecimalBlock(max_digits=8, decimal_places=2)
    description = RichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])
    bullets = ListBlock(child_block=CharBlock)
  
    class Meta:
      template = 'home/friends/blocks/plan.html'
      icon = 'tick-inverse'
      label = 'Plan'


class FriendsPageStreamBlock(StreamBlock):

  title = TitleBlock()
  subtitle = SubtitleBlock()
  plans = ListBlock(child_block=PlanBlock)
  rich_text = RichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])

