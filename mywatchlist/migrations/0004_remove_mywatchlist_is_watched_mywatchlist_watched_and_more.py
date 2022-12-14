# Generated by Django 4.1 on 2022-11-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_rename_watched_mywatchlist_is_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywatchlist',
            name='is_watched',
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='watched',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.DateField(),
        ),
    ]
