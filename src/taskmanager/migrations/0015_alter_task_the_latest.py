# Generated by Django 4.2 on 2024-01-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanager", "0014_alter_task_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="the_latest",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
