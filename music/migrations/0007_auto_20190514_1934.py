# Generated by Django 2.2.1 on 2019-05-14 19:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_track_track_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='downloads',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Downloads count'),
        ),
        migrations.AddField(
            model_name='track',
            name='likes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Likes count'),
        ),
    ]