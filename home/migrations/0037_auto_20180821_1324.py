# Generated by Django 2.0.7 on 2018-08-21 13:24

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20180821_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagegallery',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegallery',
            name='page',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length='255')), ('author', wagtail.core.blocks.CharBlock(max_length='64'))])), ('paragraph', home.moddels.blocks.ParagraphBlock()), ('gallery', home.moddels.blocks.CarouselBlock(child_block=home.moddels.blocks.ImageWithCaptionblock))], null=True),
        ),
        migrations.DeleteModel(
            name='BlogPageGallery',
        ),
    ]
