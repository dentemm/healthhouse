# Generated by Django 2.0.7 on 2018-10-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0137_healthhousesettings_error_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagefeatures',
            name='icon',
            field=models.CharField(choices=[('icon-basic_target', 'Target'), ('icon-basic_heart', 'Heart'), ('icon-ecommerce_graph3', 'Graph'), ('icon-basic_eye', 'Eye'), ('icon-basic_message_multiple', 'Text balloon')], max_length=40, null=True, verbose_name='Icon'),
        ),
    ]
