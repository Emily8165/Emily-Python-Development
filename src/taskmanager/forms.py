from django import forms

from taskmanager.models import Task


class TaskForm(forms.ModelForm):
    # define choices:
    rag_choices = [("Red", "Red"), ("Amber", "Amber"), ("Green", "Green")]
    status_choices = [
        ("Open", "Open"),
        ("In_Progress", "In_Progress"),
        ("Closed", "Closed"),
        ("Deleted", "Deleted"),
    ]
    active_choices = [(True, "True"), (False, "False")]
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
        fields = ["title", "discr", "rag", "status"]


class TaskDelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "discr", "rag", "status"]
