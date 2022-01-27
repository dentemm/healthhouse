# Generated by Django 3.1.8 on 2022-01-27 20:21

from django.db import migrations
import home.models.blocks.questions
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0198_auto_20220127_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionspage',
            name='content',
            field=wagtail.core.fields.StreamField([('subtitle', home.models.blocks.questions.SubtitleBlock()), ('paragraph', home.models.blocks.questions.ParagraphBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('gallery', home.models.blocks.questions.CarouselBlock(child_block=home.models.blocks.questions.ImageWithCaptionblock)), ('richtext', home.models.blocks.questions.CustomRichTextBlock()), ('question_answer', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=300)), ('question_asker', wagtail.core.blocks.CharBlock(max_length=64, required=False)), ('answer', wagtail.core.blocks.TextBlock(max_length=512)), ('answerer', wagtail.core.blocks.CharBlock(max_length=128, required=False))]))], null=True),
        ),
    ]
