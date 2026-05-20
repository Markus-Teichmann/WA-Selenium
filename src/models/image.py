import questionary
import os.path
from sys import platform


class Image:
    def __init__(self):
        self.path = None

    def select_image(self):
        relative_path = questionary.path("Pfad").ask()
        self.path = os.path.abspath(relative_path)

    def get_path(self):
        return self.path

    def reset(self):
        self.path = None

    def move_to_clipboard(self):
        if self.path is not None:
            if platform == "win32":
                os.system("powershell -c \"Set-Clipboard -Path '" + self.path + "'\"")
            else:
                os.system("cb copy '" + self.path + "'")