rag_choices = [("Red", "rag"), ("Amber", "rag"), ("Green", "rag")]
status_choices = [
    ("Open", "status"),
    ("In_Progress", "status"),
    ("Closed", "status"),
    ("Deleted", "status"),
]
active_choices = [(True, "True"), (False, "False")]
all_choices = [rag_choices, status_choices, active_choices]
print(all_choices)

{% if field.verbose_name != 'created on' and field.name != 'update last' and field.name != 'project' %}
    {% if field.name == "id" %}
        <td><a href="{% url 'detail' task.id %}">{{ task.id }}</a></td>
    {% else %}
        <td>{{ task|field_display:field.name|capfirst|add_line_breaks:5|linebreaks }}</td>
    {% endif %}
{% endif %}