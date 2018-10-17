# Generated by Django 2.0.7 on 2018-10-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0128_auto_20180924_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='url',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]