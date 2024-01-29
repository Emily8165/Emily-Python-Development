import os

import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from taskmanager.models import Project, Task


class TestSearch:  # this tests that a search paramiter sent through exists.
    @pytest.mark.django_db
    def test_my_search(self):
        # Arrange
        project = Project.objects.create(project_name="test")
        Task.objects.create(
            title="test_test",
            discr="test",
            rag="test",
            status="test",
            active=True,
            project=project,
        )
        # Act
        client = Client()
        response = client.get(reverse("view_tasks"), {"lookup": "test_test"})
        print(response.context)
        # Assert
        assert response.status_code == 200
        assert "test" in response.content.decode("utf-8")


class TestUser:
    @pytest.mark.django_db
    def test_my_user(self):
        # arrange
        username = "alex"
        email = "alex@alex.com"
        password = "alexiscool123"
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        # act
        client = Client()
        client.force_login(user)
        response = client.get(reverse("view_tasks"))
        # assert
        print(user)
        print(user.email)
        print(user.password)
        assert response.status_code == 200
