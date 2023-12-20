from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    discr = models.CharField(max_length=255)
    rag = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class DelTask(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.DO_NOTHING,
        related_name="del_tasks",
    )

    def __str__(self):
        return f"{self.task.title}"


# Create your models here.
