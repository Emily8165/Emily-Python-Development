# Generated by Django 4.2 on 2024-01-26 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanager", "0017_remove_task_the_latest"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="assignee",
        ),
    ]