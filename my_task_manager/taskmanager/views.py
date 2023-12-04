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

from .forms import TaskForm
from .models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "view.html"
    context_object_name = "mytask"
    paginate_by = 10
    ordering = ["id"]


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "delete.html"
    context_object_name = "task"
    success_url = "/view"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    context_object_name = "task"
    fields = ["title", "discr", "rag", "status"]
    template_name = "update.html"
    success_url = "/view"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "add.html"
    fields = ["title", "discr", "rag", "status"]
    success_url = "/view"


def taskmanager(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
