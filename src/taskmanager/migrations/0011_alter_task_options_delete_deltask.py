# Generated by Django 4.2 on 2024-01-15 13:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanager", "0010_rename_owner_task_project"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"permissions": (("can_close_tasks", "can mark tasks as closed"),)},
        ),
        migrations.DeleteModel(
            name="DelTask",
        ),
    ]
