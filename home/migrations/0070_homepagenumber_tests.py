# Generated by Django 2.0.7 on 2018-09-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_auto_20180903_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagenumber',
            name='tests',
            field=models.ManyToManyField(to='home.Bullet'),
        ),
    ]
