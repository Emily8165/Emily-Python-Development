import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from taskmanager.models import Project, Task


class TestSearch:
    @pytest.mark.django_db
    def test_my_user(self):
        # Arrange
        project = Project.objects.create(project_name="test")
        Task.objects.create(
            title="test",
            discr="test",
            rag="test",
            status="test",
            active=True,
            project=project,
        )
        # Act
        client = Client()
        response = client.get(reverse("view_tasks"), {"lookup": "task"})
        # Assert
        assert response.status_code == 200
        assert "test" in response.content.decode("utf-8")
