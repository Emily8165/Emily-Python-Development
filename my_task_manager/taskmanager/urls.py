from django.urls import path

from . import views

urlpatterns = [
    path("", views.taskmanager, name="main"),
    path("view/", views.TaskListView.as_view(), name="view_tasks"),
    path("view/detail/<pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("add/", views.add_tasks, name="add_task"),
    path("view/delete/<pk>/", views.TaskDeleteView.as_view(), name="delete"),
    path("view/update/<pk>/", views.TaskUpdateView.as_view(), name="update"),
    path("errorpage/", views.error_page, name="error_page"),
]
