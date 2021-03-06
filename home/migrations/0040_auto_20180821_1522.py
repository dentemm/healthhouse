# Generated by Django 2.0.7 on 2018-08-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_contactpage_directions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthhousesettings',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='healthhousesettings',
            name='phone_number',
            field=models.CharField(max_length=28, null=True),
        ),
        migrations.AlterField(
            model_name='healthhousesettings',
            name='tagline',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='discover_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='discover_title',
            field=models.CharField(max_length=63, null=True),
        ),
    ]
