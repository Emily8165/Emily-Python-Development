from django.urls import path

from . import views

urlpatterns = [
    path("", views.taskmanager, name="main"),
    path("view/", views.TaskListView.as_view(), name="view_tasks"),
    path("view/detail/<pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("add/", views.add_tasks, name="add_task"),
    path("view/delete/<int:id>/", views.delete, name="delete"),
    path("view/update/<int:id>/", views.update, name="update"),
    path(
        "view/updaterecord/<int:id>",
        views.updaterecord,
        name="updaterecord",
    ),
    path("errorpage/", views.error_page, name="error_page"),
]
