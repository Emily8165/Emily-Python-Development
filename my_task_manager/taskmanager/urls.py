from django.urls import path

from . import views

urlpatterns = [
    path("", views.taskmanager, name="main"),
    path("view/", views.view_tasks, name="view_tasks"),
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
