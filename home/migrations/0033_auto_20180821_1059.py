# Generated by Django 2.0.7 on 2018-08-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20180821_1055'),
    ]

    operations = [
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
