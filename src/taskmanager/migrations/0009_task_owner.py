# Generated by Django 4.2 on 2024-01-08 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanager", "0008_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="taskmanager.project",
            ),
            preserve_default=False,
        ),
    ]
