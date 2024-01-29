from django import forms
from django.contrib.auth.models import User

from taskmanager.models import Task


class TaskForm(forms.ModelForm):
    # define choices:
    user_names = [(i, i) for i in User.objects.all()]
    rag_choices = [
        ("red", "Red"),
        ("amber", "Amber"),
        ("green", "Green"),
    ]  # the second one is the one that is displayed.
    status_choices = [
        ("open", "Open"),
        ("in_progress", "In progress"),
        ("closed", "Closed"),
        ("deleted", "Deleted"),
    ]
    active_choices = [(True, "active"), (False, "inactive")]
    all_choices = (
        {"rag": rag_choices},
        {"status": status_choices},
        {"active": active_choices},
        {"user_names": user_names},
    )
    # define fields:
    title = forms.CharField(max_length=255)
    discr = forms.CharField(max_length=255)
    rag = forms.ChoiceField(choices=rag_choices)
    status = forms.ChoiceField(choices=status_choices)
    active = forms.BooleanField(required=False)

    def form_type(self):
        field_types = {}
        for field_name in self.base_fields.items():
            fields = self.base_fields[field_name[0]]
            field_types[field_name] = type(fields)
        return field_types

    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status", "active"]
        # make sure you have the fields you want to be edited in the fields part or the update won't go through!


class TaskDelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]
