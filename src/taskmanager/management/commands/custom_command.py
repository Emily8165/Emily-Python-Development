import json
import os.path

from django.core.management.base import BaseCommand, CommandParser

from ...models import Task


class Command(BaseCommand):
    help = "command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("method", type=str, help="Specify the method to execute")
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        method = options["method"]
        if method == "makered":
            self.make_red()
        elif method == "makenormal":
            self.make_normal()
        else:
            self.invalid()

    def make_red(self):
        result = "\nbody {color: red;}"
        save_path = "/Users/emilyharris/Desktop/task_manager/src/taskmanager/static/mainstatic.css"

        with open(save_path, "a") as file:
            file.write(result)

        self.stdout.write((self.style.SUCCESS("Your command has been executed!")))

    def make_normal(self):
        save_path = "/Users/emilyharris/Desktop/task_manager/src/taskmanager/static"
        file_name = "mainstatic.css"
        full_name = os.path.join(save_path, file_name)
        with open(full_name, "r") as file:
            lines = file.readlines()
        modified_lines = [line for line in lines if "body {color: red;}" not in line]
        with open(full_name, "w") as file:
            file.writelines(modified_lines)

        self.stdout.write((self.style.SUCCESS("Your command has been executed!")))

    def invalid(self):
        self.stdout.write(
            (self.style.ERROR("that is not a valid option here, please try again."))
        )
