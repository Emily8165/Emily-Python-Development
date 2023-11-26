from django.urls import path

from . import views

urlpatterns = [
    path("", views.taskmanager, name="main"),
    path("view/", views.view_tasks, name="view_tasks"),
    path("add/", views.add_tasks, name="add_task"),
    path("delete/", views.delete_tasks, name="delete_tasks"),
    path("update/", views.update_tasks, name="update_tasks"),
    path(
        "update_specific_task/", views.update_specific_task, name="update_specific_task"
    ),
]
