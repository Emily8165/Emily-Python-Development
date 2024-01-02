from typing import Any

from django import template
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

register = template.Library()

from .forms import TaskForm
from .models import DelTask, Task


class ContextDataMixim:
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["fields"] = Task._meta.fields
        context["title"] = self.title
        context["user"] = User.objects.all()
        order_by_param = self.request.GET.get("order_by")
        if order_by_param:
            context["filter"] = Task.objects.order_by(order_by_param)
        else:
            context["filter"] = Task.objects.all()

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
        initial_order = self.request.GET.get("order")  #
        default_order = (
            "title"
            if initial_order not in [f.name for f in Task._meta.get_fields()]
            else initial_order
        )
        order_by = self.request.GET.get("order_by", default_order)
        return Task.objects.all().order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_by"] = self.request.GET.get("order_by")
        return context


class TaskDetailView(ContextDataMixim, generic.DetailView):
    model = Task
    title = "Detailed"
    template_name = "task_detail.html"
    context_object_name = "task"


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

    def get_queryset(self):
        query = self.request.GET.get("lookup", "")
        object_list = Task.objects.filter(Q(title__icontains=query))
        return object_list

    """
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
    """

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


class UserView(generic.DetailView):
    model = User
    title = "User view"
    template_name = "user_actions.html"
    context_object_name = "specified_user"

    def get_object(
        self, queryset: QuerySet[Any] | None = ...
    ) -> Model:  # this method gets a specific object
        # as specified by what is being passed over to the view by the URL paramiters.
        # in this case 'i' is being sent over the url so it is the object that is being picked up by the method.
        specified_user = self.kwargs.get(
            "i"
        )  # this specifies the request and the data attributed to the object and attaches it to the item specified_user.
        return User.objects.filter(
            username=specified_user
        ).first()  # this searches for the object in the model and filters out all others and returns the user.

    def get_context_data(
        self, **kwargs: Any
    ) -> dict[
        str, Any
    ]:  # this holds data for the template. we are using a specific method here instead of the contextdatamixim as the context data mixim doesn't work with detailviews
        context = super().get_context_data(**kwargs)
        context[
            "title"
        ] = (
            self.title
        )  # it holds data as a dictionary to be called hence why we have context["data"] = information saved in the "data".
        context["fields"] = Task._meta.fields
        return context

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> (
        HttpResponse
    ):  # this handles https responses and returns all other data above in the template
        return super().get(request, *args, **kwargs)


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
