from typing import Any

from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic

from .forms import TaskForm
from .models import DelTask, Task


class ContextDataMixim:
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["fields"] = Task._meta.fields
        context["title"] = self.title
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

    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.all().filter(active=True)

    def filter_view(self, *args, **kwargs):
        filter_order = Task.objects.all().order_by("title").values()
        print("filter_order:", filter_order)
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context["filter_order"] = filter_order
        return context


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

    def copy(self):
        model = DelTask

        pass


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
        DelTask.objects.create(task=form.instance)
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

    def get_queryset(
        self,
    ) -> QuerySet[Any]:  # this retirives the objects from the list view.
        lookup_param = self.request.GET.get(
            "lookup", ""
        )  # this retireves the specific data from the query set. The look up is a paramiter set in the GET function.
        # Filter tasks based on the search parameter
        matching_tasks = Task.objects.filter(
            title__icontains=lookup_param
        )  # this compares the data to all object in the model and filters out any that aren't define in the look up paraiter.
        return matching_tasks

    def get(self, request, *args, **kwargs):  # this returns the data as a list view.
        # Call the parent get method to handle the ListView logic
        response = super().get(request, *args, **kwargs)
        return response

    # the goal here is not to reproduce the searched for object but to direct to the detailed view of it.


class ViewHistory(ContextDataMixim, generic.ListView):
    model = DelTask
    title = "view_history"
    template_name = "view_history.html"
    context_object_name = "model"
    paginate_by = 10
    ordering = ["id"]


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
