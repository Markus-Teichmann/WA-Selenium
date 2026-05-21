import questionary
import os.path
from sys import platform

class Document:
    def __init__(self):
        self.relative_path = None
        self.absolute_path = None

    def select_document(self):
        self.relative_path = questionary.path("Pfad").ask().strip()
        self.absolute_path = os.path.abspath(self.relative_path).strip()

    def get_path(self):
        if platform == "win32":
            return self.absolute_path
        else:
            return self.relative_path

    def reset(self):
        self.relative_path = None
        self.absolute_path = None

    def move_to_clipboard(self):
        if self.relative_path is not None:
            if platform == "win32":
                os.system("powershell -c \"Set-Clipboard -Path '" + self.absolute_path + "'\"")
            else:
                os.system("cb copy " + self.relative_path)