# Generated by Django 2.0.7 on 2018-08-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0025_partnerpage_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='discover_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='discover_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='discover_title',
            field=models.CharField(max_length=63, null=True),
        ),
    ]
