# Generated by Django 2.1.15 on 2020-04-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0172_auto_20200407_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronaarticlepage',
            name='related_title',
            field=models.CharField(default='Related articles', max_length=64, verbose_name='Title related art.'),
        ),
    ]