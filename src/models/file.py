import questionary
import os.path

class File:
    def __init__(self):
        self.relative_path = None
        self.absolute_path = None

    def select_file(self):
        self.relative_path = questionary.path("Pfad").ask().strip()
        self.absolute_path = os.path.abspath(self.relative_path).strip()

    def get_path(self):
        return self.absolute_path

    def reset(self):
        self.relative_path = None
        self.absolute_path = None