# Generated by Django 3.0.3 on 2020-02-13 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
