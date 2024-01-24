# change title to a slug field, add an update field, delete slug
from django.db import migrations, models
from django.utils.text import slugify

from taskmanager.models import Task


class Migration(migrations.Migration):
    dependencies = [("taskmanager", "0012_task_slug")]

    operations = [
        migrations.AddField(
            model_name="task",
            name="the_latest",
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
    ]
