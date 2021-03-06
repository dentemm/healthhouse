# Generated by Django 2.1.7 on 2019-03-16 09:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0141_auto_20190228_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('when', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PublicEvent',
            fields=[
                ('calendaritem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.CalendarItem')),
                ('max_attendees', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
            bases=('home.calendaritem',),
        ),
        migrations.AddField(
            model_name='calendaritem',
            name='image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
    ]
