# Generated by Django 2.0.7 on 2018-09-11 19:22

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_auto_20180911_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discoverypage',
            name='content',
            field=wagtail.core.fields.StreamField([('parallax', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=64)), ('info_text', wagtail.core.blocks.CharBlock(max_length=255)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'HH blue'), ('white', 'White'), ('dark-blue', 'HH dark')])), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), required=False)), ('external_links2', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('url_title', wagtail.core.blocks.CharBlock(max_length=28, required=False))]), required=False))]))], null=True),
        ),
    ]
