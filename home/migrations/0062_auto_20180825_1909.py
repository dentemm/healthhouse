# Generated by Django 2.0.7 on 2018-08-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_auto_20180825_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='feature_text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
