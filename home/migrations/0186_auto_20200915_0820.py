# Generated by Django 3.1.1 on 2020-09-15 08:20

from django.db import migrations, models
import django.db.models.deletion
import home.models.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0052_pagelogentry'),
        ('home', '0185_contactpageformfield_clean_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendaritem',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='SOPPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(null=True)),
                ('content', wagtail.core.fields.StreamField([('subtitle', home.models.blocks.SubtitleBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(max_length=255)), ('author', wagtail.core.blocks.CharBlock(max_length=64))])), ('paragraph', home.models.blocks.ParagraphBlock()), ('gallery', home.models.blocks.CarouselBlock(child_block=home.models.blocks.ImageWithCaptionblock)), ('unordered_list', home.models.blocks.CustomListBlock(child_block=home.models.blocks.ListItemBlock)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('rich_text', home.models.blocks.CustomRichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul'])), ('embed', home.models.blocks.CustomEmbedBlock()), ('link', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(max_lenght=64, required=True)), ('internal_link', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))], null=True)),
                ('cover_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]