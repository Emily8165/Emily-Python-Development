# Generated by Django 4.2.1 on 2023-12-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RecentlyDeletedTasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("del_title", models.CharField(max_length=255)),
                ("del_discr", models.CharField(max_length=255)),
                ("del_rag", models.CharField(max_length=255)),
                ("del_status", models.CharField(max_length=255)),
            ],
        ),
    ]
