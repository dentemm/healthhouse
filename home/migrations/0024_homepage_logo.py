# Generated by Django 2.0.7 on 2018-08-19 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('home', '0023_auto_20180809_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
