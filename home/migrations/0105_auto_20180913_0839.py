# Generated by Django 2.0.7 on 2018-09-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0104_discoverydetailpage_discover_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthhousesettings',
            name='account',
            field=models.CharField(max_length=24, null=True, verbose_name='Account number'),
        ),
        migrations.AddField(
            model_name='healthhousesettings',
            name='vat_number',
            field=models.CharField(max_length=16, null=True, verbose_name='VAT / BTW'),
        ),
    ]
