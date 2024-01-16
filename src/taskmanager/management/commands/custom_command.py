import json

from django.core.management.base import BaseCommand

from ...models import Task


class Command(BaseCommand):
    help = "command"

    def handle(self, *args, **options):
        result = "colour: red;"
        with open("mainstatic.css", "w") as file:  # w means write.
            file.write(result)

        self.stdout.write((self.style.SUCCESS("Your command has been executed!")))
