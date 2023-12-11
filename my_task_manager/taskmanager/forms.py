from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    rag_choices = {"option_1": "Red", "option_2": "Amber", "option_3": "Green"}
    rag = forms.ChoiceField(choices=rag_choices.items())
    status_choices = {
        "option_1": "Open",
        "option_2": "In_progress",
        "option_3": "In_test",
    }
    status = forms.ChoiceField(choices=status_choices.items())

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
