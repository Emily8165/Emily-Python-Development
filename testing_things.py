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
