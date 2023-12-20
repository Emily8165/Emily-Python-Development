from django.test import TestCase
from taskmanager.models import Task


class ModelsTestCase(TestCase()):
    def setup(self):
        Task.objects.all()


# You can write a test to see if there are any values in the cells in the model that don't start with a capital.
