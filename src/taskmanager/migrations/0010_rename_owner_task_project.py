# Generated by Django 4.2 on 2024-01-08 21:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanager", "0009_task_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="owner",
            new_name="project",
        ),
    ]
