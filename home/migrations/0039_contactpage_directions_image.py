# Generated by Django 2.0.7 on 2018-08-21 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('home', '0038_auto_20180821_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='directions_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
