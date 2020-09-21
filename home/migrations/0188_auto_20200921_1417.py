# Generated by Django 3.1.1 on 2020-09-21 14:17

from django.db import migrations
import home.models.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0187_homepage_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soppage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.models.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length=255)), ('author', wagtail.core.blocks.CharBlock(max_length=64))])), ('paragraph', home.models.blocks.ParagraphBlock()), ('gallery', home.models.blocks.CarouselBlock(child_block=home.models.blocks.ImageWithCaptionblock)), ('unordered_list', home.models.blocks.CustomListBlock(child_block=home.models.blocks.ListItemBlock)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('rich_text', home.models.blocks.CustomRichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])), ('embed', home.models.blocks.CustomEmbedBlock()), ('link', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(max_lenght=64, required=True)), ('internal_link', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))])), ('intro', home.models.blocks.IntroBlock())], null=True),
        ),
    ]
