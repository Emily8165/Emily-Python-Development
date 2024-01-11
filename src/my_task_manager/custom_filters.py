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


@register.filter(name="field_display")
def field_display(task, field_name):
    return getattr(task, field_name, "")
