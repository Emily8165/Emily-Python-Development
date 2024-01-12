from django.contrib.auth.models import User
from django.db import models


def default_user_function():
    return User.objects.first()


class Project(models.Model):
    project_name = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=255)
    discr = models.CharField(max_length=255)
    rag = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    update_last = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        permissions = (("can_close_tasks", "can mark tasks as closed"),)

    def __str__(self):
        return f"{self.title}"


class DelTask(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name="del_tasks",
    )

    def __str__(self):
        return f"{self.task.title}"


# Create your models here.
