# Generated by Django 4.2 on 2024-01-01 13:30
from datetime import date

import django.db.models.deletion
from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taskmanager", "0005_alter_task_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="created_on",
            field=models.DateField(auto_now_add=True, default=date.today()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="update_last",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
