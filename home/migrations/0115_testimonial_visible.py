# Generated by Django 2.0.7 on 2018-09-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0114_auto_20180913_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
