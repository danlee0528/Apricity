# Generated by Django 3.0.3 on 2020-02-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
