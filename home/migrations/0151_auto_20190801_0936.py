# Generated by Django 2.1.7 on 2019-08-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0150_auto_20190530_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_type',
            field=models.IntegerField(choices=[(1, 'Founding partner'), (2, 'Structural partner'), (3, 'Other partner'), (4, 'No partner'), (5, 'Trusted member')], null=True),
        ),
    ]
