# Generated by Django 2.0.7 on 2018-10-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0138_auto_20181022_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='thank_you_text',
            field=models.CharField(default='Thank you for your message!', max_length=160),
        ),
    ]
