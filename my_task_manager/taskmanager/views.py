from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse

from .forms import TaskForm
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


def delete(request, id):
    mytaskid = Task.objects.get(id=id)
    mytaskid.delete()
    return HttpResponseRedirect(reverse("view_tasks"))


def update(request, id):
    myupdate = Task.objects.get(id=id)
    template = loader.get_template("update.html")
    mytask = Task.objects.all()
    model_fields = Task._meta.get_fields()
    column_headers = [field.name for field in model_fields if field.concrete]
    context = {"myupdate": myupdate, "titles": column_headers, "mytask": mytask}
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    title = request.POST["title"]
    discr = request.POST["discr"]
    rag = request.POST["rag"]
    status = request.POST["status"]
    myupdate = Task.objects.get(id=id)
    myupdate.title = title
    myupdate.discr = discr
    myupdate.rag = rag
    myupdate.status = rag
    myupdate.save()
    return HttpResponseRedirect(reverse("view_tasks"))


def error_page(request):
    template = loader.get_template("errorpage.html")
    return HttpResponse(template.render())


# Create your views here.
