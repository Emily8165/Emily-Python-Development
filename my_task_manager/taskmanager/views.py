from typing import Any

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


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "delete.html"
    context_object_name = "task"
    success_url = "/view"


class TaskUpdateView(generic.UpdateView):
    model = Task
    context_object_name = "task"
    fields = ["title", "discr", "rag", "status"]
    template_name = "update.html"
    success_url = "/view"


class TaskCreateView(generic.CreateView):
    pass


def taskmanager(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def add_tasks(request):
    template = loader.get_template("add.html")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view")
    else:
        form = TaskForm()
        return render(request, "add.html", {"form": form})


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
