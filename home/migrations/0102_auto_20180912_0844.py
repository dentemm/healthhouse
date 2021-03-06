# Generated by Django 2.0.7 on 2018-09-12 08:44

from django.db import migrations
import home.models.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0101_auto_20180912_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.models.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length=255)), ('author', wagtail.core.blocks.CharBlock(max_length=64))])), ('paragraph', home.models.blocks.ParagraphBlock()), ('gallery', home.models.blocks.CarouselBlock(child_block=home.models.blocks.ImageWithCaptionblock)), ('unordered_list', home.models.blocks.CustomListBlock(child_block=home.models.blocks.ListItemBlock)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('rich_text', home.models.blocks.CustomRichTextBlock()), ('embed', home.models.blocks.CustomEmbedBlock())], null=True),
        ),
    ]
