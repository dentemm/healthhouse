# Generated by Django 2.0.7 on 2018-09-13 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0107_expoarea_meetingroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyline',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Partner'),
        ),
    ]