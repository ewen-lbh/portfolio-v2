# Generated by Django 2.2.1 on 2019-05-09 19:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Collection title')),
                ('cover_color', models.CharField(max_length=5, verbose_name="Cover art's color dominant")),
                ('kind', models.CharField(max_length=6, verbose_name='Kind/type')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Track title')),
                ('artist', models.CharField(default='Mx3', max_length=50, verbose_name='Artist')),
                ('is_remix', models.BooleanField(verbose_name='The track is a remix ?')),
                ('duration', models.DurationField(verbose_name='Track duration')),
                ('work_time', models.DurationField(verbose_name='Work time')),
                ('video_url', models.CharField(max_length=100, verbose_name='YouTube video URL')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Collection', verbose_name="Track's collection")),
            ],
            options={
                'verbose_name': 'track',
                'verbose_name_plural': 'tracks',
            },
        ),
    ]
