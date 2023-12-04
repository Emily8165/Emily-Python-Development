from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    discr = models.CharField(max_length=255)
    rag = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"


# Create your models here.
