# Generated by Django 3.0.3 on 2020-02-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200213_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
