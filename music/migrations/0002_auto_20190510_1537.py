# Generated by Django 2.2.1 on 2019-05-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='kind',
            field=models.CharField(choices=[('EP', 'EP'), ('SG', 'Single'), ('AB', 'Album')], max_length=6, verbose_name='Kind/type'),
        ),
    ]
