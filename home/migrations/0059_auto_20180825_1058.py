# Generated by Django 2.0.7 on 2018-08-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_homepagevisitors'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='visit_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='visit_title',
            field=models.CharField(max_length=63, null=True),
        ),
    ]
