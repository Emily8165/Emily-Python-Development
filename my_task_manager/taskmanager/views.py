from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import TaskForm, TaskUpdateForm
from .models import Task


def taskmanager(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def view_tasks(request):
    mytask = Task.objects.all()
    model_fields = Task._meta.get_fields()
    column_headers = [field.name for field in model_fields if field.concrete]
    context = {"mytask": mytask, "titles": column_headers}
    template = loader.get_template("view.html")
    return HttpResponse(template.render(context, request))


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


def delete_tasks(request):
    mytask = Task.objects.all()
    model_fields = Task._meta.get_fields()
    column_headers = [field.name for field in model_fields if field.concrete]
    context = {"mytask": mytask, "titles": column_headers}
    template = loader.get_template("delete.html")
    selected_tasks = request.POST.getlist("chosen_task")
    try:
        if request.method == "POST":
            for task_id in selected_tasks:
                taskdel = get_object_or_404(Task, pk=task_id)
                taskdel.delete()
                return redirect("/view")
    except:
        return render(request, "delete.html")
    return HttpResponse(template.render(context, request))


def update_tasks(request):
    template = loader.get_template("update.html")
    mytask = Task.objects.all()
    model_fields = Task._meta.get_fields()
    column_headers = [field.name for field in model_fields if field.concrete]
    myform = TaskUpdateForm()
    context = {"mytask": mytask, "titles": column_headers, "myform": myform}
    try:
        if request.method == "POST":
            return redirect("/update_specific_task")
    except:
        return redirect("/errorpage")
    return HttpResponse(template.render(context, request))


def update_specific_task(request):
    template = loader.get_template("update_specific_task.html")
    mytask = Task.objects.all()
    model_fields = Task._meta.get_fields()
    selected_task = request.POST.get("submit_choice")
    column_headers = [field.name for field in model_fields if field.concrete]
    myform = TaskUpdateForm()
    context = {
        "mytask": mytask,
        "titles": column_headers,
        "myform": myform,
        "chosen": selected_task,
    }
    """
    try:
        if request.method == "POST":
            return redirect("/view")
    except:
        return render(request, "update.html")
    """
    return HttpResponse(template.render(context, request))


# Create your views here.
