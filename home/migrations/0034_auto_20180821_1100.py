# Generated by Django 2.0.7 on 2018-08-21 11:00

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20180821_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthhousesettings',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='healthhousesettings',
            name='phone_number',
            field=models.CharField(default='+0123456789', max_length=28, null=True),
        ),
        migrations.AlterField(
            model_name='healthhousesettings',
            name='tagline',
            field=models.CharField(default='Some random tagline', max_length=255, null=True),
        ),
    ]
