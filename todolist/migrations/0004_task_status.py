# Generated by Django 4.1 on 2022-09-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0003_task_is_finished"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(default="Belum Selesai", max_length=13),
        ),
    ]