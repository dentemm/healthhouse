# Generated by Django 3.1.8 on 2022-02-04 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0202_auto_20220204_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsoverview',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
