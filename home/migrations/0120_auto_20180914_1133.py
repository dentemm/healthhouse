# Generated by Django 2.0.7 on 2018-09-14 11:33

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0119_discoverydetailpage_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoomBullet',
            fields=[
                ('generalbullet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.GeneralBullet')),
                ('expo_area', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='home.MeetingRoom')),
            ],
            bases=('home.generalbullet',),
        ),
        migrations.AlterField(
            model_name='discoverydetailpage',
            name='discover_detail',
            field=models.CharField(choices=[('storylines', 'Storylines'), ('meeting_rooms', 'Meeting rooms'), ('expo_rooms', 'Exhibition areas'), ('projects', 'Projects')], max_length=28, null=True, verbose_name='Page type'),
        ),
    ]