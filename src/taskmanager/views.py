from typing import Any

from django import template
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, Permission, User
from django.db import models
from django.db.models import Q
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest
from django.http import HttpResponse
from django.http import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django_filters import FilterSet

register = template.Library()

from .forms import TaskForm
from .models import Task


class ContextDataMixim:
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["Tasks"] = Task.objects.all()
        context["user"] = User.objects.all()
        context["groups"] = Group.objects.all()
        context["permissions"] = Permission.objects.all()
        context["fields"] = Task._meta.get_fields()
        order_by_param = self.request.GET.get("order_by")
        if order_by_param:
            context["filter"] = Task.objects.order_by(order_by_param)
        else:
            context["filter"] = Task.objects.all()
        context["field_form_type"] = TaskForm().form_type()
        return context


class Basic_layout(ContextDataMixim, generic.ListView):
    model = Task
    template_name = "base_layout"
    context_object_name = "model"


class TaskListView(ContextDataMixim, generic.ListView):
    model = Task
    title = "View"
    template_name = "view.html"
    context_object_name = "model"
    paginate_by = 10
    ordering = ["id"]
    fields = Task._meta.get_fields()

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        new_order = self.request.GET.get("order_by")
        default = (
            "title"
            if new_order not in [f.name for f in Task._meta.get_fields()]
            else new_order
        )
        if self.request.GET.get:
            for param, value in self.request.GET.items():
                if param == "order_by" or param == "page":
                    continue
                queryset = queryset.filter(Q(**{f"{param}": f"{value}"}))
        return queryset.order_by(default)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_choices"] = TaskForm.all_choices
        context["fields"] = Task._meta.get_fields()
        return context

    def error_page(self):
        return render(self.request, "errorpage.html")


class TaskDetailView(ContextDataMixim, generic.DetailView):
    model = Task
    title = "Detailed"
    template_name = "task_detail.html"
    context_object_name = "task"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("pk")
        return get_object_or_404(Task, pk=pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["Tasks"] = [self.get_object()]
        return context


class TaskDeleteView(ContextDataMixim, LoginRequiredMixin, generic.DeleteView):
    model = Task
    title = "Delete"
    template_name = "delete.html"
    context_object_name = "task"
    fields = ["title", "discr", "rag", "status"]
    success_url = "/view"


class TaskUpdateView(ContextDataMixim, LoginRequiredMixin, generic.UpdateView):
    model = Task
    title = "Update"
    form_class = TaskForm
    template_name = "update.html"
    context_object_name = "task"
    success_url = "/view"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    title = "Add"
    form_class = TaskForm
    template_name = "add.html"
    success_url = "/view"

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class MainView(generic.TemplateView):
    model = Task
    title = "Home"
    template_name = "main.html"


class SearchView(generic.ListView):
    model = Task
    template_name = "search.html"
    context_object_name = "tasks"
    form_class = TaskForm

    def get_queryset(self):
        query = self.request.GET.get("lookup", "")
        object_list = Task.objects.filter(Q(title__icontains=query))
        return object_list

    def get(self, request, *args, **kwargs):  # this returns the data as a list view.
        # Call the parent get method to handle the ListView logic
        response = super().get(request, *args, **kwargs)
        return response

    # the goal here is not to reproduce the searched for object but to direct to the detailed view of it.


class ViewHistory(ContextDataMixim, generic.ListView):
    model = Task
    title = "view_history"
    template_name = "view_history.html"
    context_object_name = "model"
    paginate_by = 10
    ordering = ["id"]


class UserView(generic.DetailView):
    model = User
    title = "User view"
    template_name = "user_actions.html"
    context_object_name = "specified_user"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        specified_user = self.kwargs.get("i")
        user = get_object_or_404(User, username=specified_user)
        user_group = user.groups.all()
        raw_permissions = user.user_permissions.all()
        list_of_permission_names = []
        x = [
            list_of_permission_names.append(permissions.name)
            for permissions in raw_permissions
        ]
        permissions = []
        y = [
            permissions.append(str(per).strip("Can add"))
            for count, per in enumerate(list_of_permission_names)
            if count % 4 == 0
        ]

        ob = {
            "user": user,
            "user_group": user_group,
            "permissions": permissions,
        }
        return ob

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["fields"] = Task._meta.fields
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


class SettingsView(ContextDataMixim, generic.TemplateView):
    title = "Task Settings"
    template_name = "settings.html"


class OrgChartView(ContextDataMixim, generic.TemplateView):
    model = User
    title = "Orginisation Chart"
    template_name = "org_chart.html"
    context_object_name = "object"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        users = User.objects.all()
        groups = Group.objects.all()
        permissions = Permission.objects.all()
        user_groups = {}
        for user in users:
            user_groups[user] = user.groups.all()
        context = {
            "users": users,
            "groups": groups,
            "user_groups": user_groups,
            "permissions": permissions,
        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
