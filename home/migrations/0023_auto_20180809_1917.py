# Generated by Django 2.0.7 on 2018-08-09 19:17

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20180809_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.TextBlock(icon='edit')), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))]), label='Image gallery', min=3)), ('gallery', home.models.blocks.CarouselBlock(child_block=home.models.blocks.ImageWithCaptionblock))], null=True),
        ),
    ]
