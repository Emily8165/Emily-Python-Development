from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]


class TaskDelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]
