# Generated by Django 2.0.7 on 2018-09-03 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('home', '0080_homepagenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='number_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='number_title',
            field=models.CharField(max_length=63, null=True, verbose_name='title'),
        ),
    ]
