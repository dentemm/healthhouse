# Generated by Django 2.0.7 on 2018-08-23 18:59

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_auto_20180823_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length='255')), ('author', wagtail.core.blocks.CharBlock(max_length='64'))])), ('paragraph', home.blocks.ParagraphBlock()), ('gallery', home.blocks.CarouselBlock(child_block=home.blocks.ImageWithCaptionblock)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('rich_text', home.blocks.CustomRichTextBlock()), ('embed', home.blocks.CustomEmbedBlock())], null=True),
        ),
    ]