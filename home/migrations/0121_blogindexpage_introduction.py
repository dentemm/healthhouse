# Generated by Django 2.0.7 on 2018-09-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0120_auto_20180914_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='introduction',
            field=models.TextField(null=True),
        ),
    ]