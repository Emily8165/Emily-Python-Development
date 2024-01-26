import pytest
from django.contrib.auth.models import User

from taskmanager.models import Task
from taskmanager.views import TaskListView


@pytest.mark.django_db(True)
def test_first():
    assert TaskListView()
