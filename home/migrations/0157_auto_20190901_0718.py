# Generated by Django 2.1.7 on 2019-09-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0156_eventvisitor_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventvisitor',
            name='brings_guest',
        ),
        migrations.AlterField(
            model_name='eventvisitor',
            name='company',
            field=models.CharField(max_length=30, verbose_name='Company / Organisation'),
        ),
        migrations.AlterField(
            model_name='eventvisitor',
            name='email',
            field=models.EmailField(max_length=90, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='eventvisitor',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='eventvisitor',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Last name'),
        ),
    ]
