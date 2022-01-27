# Generated by Django 3.1.8 on 2022-01-27 17:32

from django.db import migrations, models
import django.db.models.deletion
import home.models.blocks.questions
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0195_questionsoverview_questionspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsoverview',
            name='info_text',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='questionspage',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', home.models.blocks.questions.ParagraphBlock()), ('gallery', home.models.blocks.questions.CarouselBlock(child_block=home.models.blocks.questions.ImageWithCaptionblock)), ('richtext', home.models.blocks.questions.CustomRichTextBlock())], null=True),
        ),
        migrations.AddField(
            model_name='questionspage',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
