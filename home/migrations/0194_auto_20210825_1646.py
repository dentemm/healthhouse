# Generated by Django 3.1.8 on 2021-08-25 16:46

from django.db import migrations
import home.models.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0193_coronaarticlepage_fullwidth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronaarticlepage',
            name='fullwidth',
            field=wagtail.core.fields.StreamField([('gallery', home.models.blocks.CoronaCarouselBlock(child_block=home.models.blocks.CoronaImageBlock)), ('embed', home.models.blocks.CoronaEmbedBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronaarticlepage',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('gif_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('embed', home.models.blocks.CoronaEmbedBlock()), ('gallery', home.models.blocks.CoronaCarouselBlock(child_block=home.models.blocks.CoronaImageBlock))], blank=True, null=True),
        ),
    ]
