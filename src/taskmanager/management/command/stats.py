from django.core.management.base import BaseCommand

from ...models import DelTask, Task


class Command(BaseCommand):
    help = "Displays stats related to Article and Comment models"
    num = []
    for o in Task.objects.all():
        num.append(o)
    print(num)
