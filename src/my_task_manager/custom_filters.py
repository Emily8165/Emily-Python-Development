import django_filters
from django import template

from taskmanager.models import Task

register = template.Library()


@register.filter(name="add_line_breaks")
def add_line_breaks(inputted, line_break_num):
    words = inputted.split()
    result = []

    for i, word in enumerate(words, start=1):
        result.append(word)
        if i % line_break_num == 0 and i != len(words):
            result.append("\n")
    result = " ".join(result)
    return result


class TaskFilter(django_filters.FilterSet):
    id = django_filters.RangeFilter()

    class Meta:
        model = Task
        fields = {
            "title": ["icontains"],
            "discr": ["icontains"],
            "rag": ["exact"],
            "status": ["exact"],
            "active": ["exact"],
        }
