# Generated by Django 2.0.7 on 2018-08-23 14:03

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20180823_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length='255')), ('author', wagtail.core.blocks.CharBlock(max_length='64'))])), ('paragraph', home.blocks.ParagraphBlock()), ('gallery', home.blocks.CarouselBlock(child_block=home.blocks.ImageWithCaptionblock)), ('rich_text', home.blocks.CustomRichTextBlock()), ('embed', home.blocks.CustomEmbedBlock()), ('other', wagtail.embeds.blocks.EmbedBlock())], null=True),
        ),
    ]
