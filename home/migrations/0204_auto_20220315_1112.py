# Generated by Django 3.1.8 on 2022-03-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0203_questionsoverview_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directionsbullets',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='expoareabullet',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='generalbullet',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='meetingroombullet',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='projectbullet',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='storylinebullet',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='generalbullet',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]