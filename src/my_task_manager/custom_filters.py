from django import template

register = template.Library()


@register.filter(name="add_line_breaks")
def add_line_breaks(inputted, line_break_num):
    x = str(inputted)
    words = x.split()
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


"""the getattr method works by trying to find an attribute in an object. like a field in a task. """
