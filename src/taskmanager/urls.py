from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("admin/", admin.site.urls, name="admin2"),
    path("view/", views.TaskListView.as_view(), name="view_tasks"),
    path("view/view_history/", views.ViewHistory.as_view(), name="view_history"),
    path("view/detail/<pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("view/create", views.TaskCreateView.as_view(), name="create"),
    path("view/delete/<pk>/", views.TaskDeleteView.as_view(), name="delete"),
    path("view/update/<pk>/", views.TaskUpdateView.as_view(), name="update"),
    path("view/search/", views.SearchView.as_view(), name="search"),
    path("view/user/<i>", views.UserView.as_view(), name="user_view"),
    path("errorpage/", views.error_page, name="error_page"),
    path("view/settings/", views.SettingsView.as_view(), name="settings"),
    path("view/org_chart", views.OrgChartView.as_view(), name="org"),
]
