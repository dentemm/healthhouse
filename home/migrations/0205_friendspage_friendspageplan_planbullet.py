# Generated by Django 3.2.17 on 2023-03-12 19:10

from django.db import migrations, models
import django.db.models.deletion
import home.models.blocks.friends
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0204_auto_20220315_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('title', home.models.blocks.friends.TitleBlock()), ('subtitle', home.models.blocks.friends.SubtitleBlock()), ('plans', wagtail.core.blocks.ListBlock(child_block=home.models.blocks.friends.PlanBlock)), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'ol', 'ul']))])),
                ('contact_name', models.CharField(max_length=164)),
                ('contact_title', models.CharField(max_length=164)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=24)),
                ('contact_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('cover_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FriendsPagePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='home.friendspage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlanBullet',
            fields=[
                ('generalbullet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.generalbullet')),
                ('plan', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='home.friendspageplan')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('home.generalbullet',),
        ),
    ]