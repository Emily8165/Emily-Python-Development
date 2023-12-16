from typing import Any

from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from .forms import TaskForm
from .models import Task


class ContextDataMixim:
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["fields"] = Task._meta.fields
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


class TaskDetailView(ContextDataMixim, generic.DetailView):
    model = Task
    title = "Detailed"
    template_name = "task_detail.html"
    context_object_name = "task"
    fields = ["title", "discr", "rag", "status"]


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


class MainView(generic.TemplateView):
    model = Task
    title = "Home"
    template_name = "main.html"


class SearchView(generic.ListView):
    model = Task
    template_name = "search.html"
    context_object_name = "tasks"
    form_class = TaskForm

    def get_queryset(self) -> QuerySet[Any]:
        lookup_param = self.request.GET.get("lookup", "")
        # Filter tasks based on the search parameter
        matching_tasks = Task.objects.filter(title__icontains=lookup_param)
        return matching_tasks

    def get(self, request, *args, **kwargs):
        # Call the parent get method to handle the ListView logic
        response = super().get(request, *args, **kwargs)
        return response

    # the goal here is not to reproduce the searched for object but to direct to the detailed view of it.


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
