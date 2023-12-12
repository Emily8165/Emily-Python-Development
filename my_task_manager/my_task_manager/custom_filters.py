import math

from django import template

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
