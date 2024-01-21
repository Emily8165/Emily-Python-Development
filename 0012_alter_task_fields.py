from django.db import migrations, models

from taskmanager.models import Task


class Migration(migrations.Migration):
    dependencies = [
        (
            "taskmanager",
            "0010_rename_owner_task_project.py",
        ),
    ]
    operations = [
        migrations.RenameField(
            model_name="Task",
            old_name="task",
            new_name="Title",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="discr",
            new_name="Discr",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="rag",
            new_name="Rag",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="status",
            new_name="Status",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="active",
            new_name="Active",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="title",
            new_name="Title",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="created_on",
            new_name="Created_on",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="updated_last",
            new_name="Updated_last",
        ),
        migrations.RenameField(
            model_name="Task",
            old_name="project",
            new_name="Project",
        ),
    ]
