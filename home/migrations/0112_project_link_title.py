# Generated by Django 2.0.7 on 2018-09-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0111_auto_20180913_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
