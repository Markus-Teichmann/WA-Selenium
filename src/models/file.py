import base64
import mimetypes

import questionary
import os.path

class File:
    def __init__(self):
        self.relative_path = None
        self.absolute_path = None
        self.type = None
        self.content = None
        self.name = None

    def select_file(self):
        self.relative_path = questionary.path("Pfad").ask().strip()
        self.absolute_path = os.path.abspath(self.relative_path).strip()
        mime_type, encoding = mimetypes.guess_type(self.absolute_path)
        self.type = mime_type
        self.content = base64.b64encode(open(self.absolute_path, 'rb').read()).decode('utf8')
        self.name = os.path.basename(self.absolute_path)

    def get_path(self):
        return self.absolute_path

    def get_type(self):
        return self.type

    def get_content(self):
        return self.content

    def get_name(self):
        return self.name

    def reset(self):
        self.relative_path = None
        self.absolute_path = None
        self.type = None
        self.content = None
        self.name = None