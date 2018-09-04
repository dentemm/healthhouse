# Generated by Django 2.0.7 on 2018-08-22 12:13

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20180822_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.moddels.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length='255')), ('author', wagtail.core.blocks.CharBlock(max_length='64'))])), ('paragraph', home.moddels.blocks.ParagraphBlock()), ('gallery', home.moddels.blocks.CarouselBlock(child_block=home.moddels.blocks.ImageWithCaptionblock)), ('rich_text', home.moddels.blocks.CustomRichTextBlock())], null=True),
        ),
    ]
