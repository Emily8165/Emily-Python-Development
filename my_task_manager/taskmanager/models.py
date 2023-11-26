from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    discr = models.CharField(max_length=255)
    rag = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


# Create your models here.
