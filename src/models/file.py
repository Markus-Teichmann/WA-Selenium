import base64
import mimetypes

import questionary
import os.path

class File:
    def __init__(self, relative_path=None, absolute_path=None, type=None, content=None, name=None):
        self.relative_path = relative_path
        self.absolute_path = absolute_path
        self.type = type
        self.content = content
        self.name = name

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

    def serialize(self):
        if self is None or self.absolute_path is None or self.relative_path is None or self.type is None or self.content is None or self.name is None:
            return None
        return ('{' +
            '\"relative_path\": \"' + base64.b64encode(self.relative_path.encode('utf8')).decode('utf8') + '\", ' +
            '\"absolute_path\": \"' + base64.b64encode(self.absolute_path.encode('utf8')).decode('utf8') + '\", ' +
            '\"type\": \"' + base64.b64encode(self.type.encode('utf8')).decode('utf8') + '\", ' +
            '\"content\": \"' + self.content + '\", ' +
            '\"name\": \"' + base64.b64encode(self.name.encode('utf8')).decode('utf8') +
        '\"}')

    @staticmethod
    def parse(json: dict):
        if ('relative_path' in json and
            'absolute_path' in json and
            'type' in json and
            'content' in json and
            'name' in json):
            return File(
                base64.b64decode(json['relative_path'].encode('utf8')).decode('utf8'),
                base64.b64decode(json['absolute_path'].encode('utf8')).decode('utf8'),
                base64.b64decode(json['type'].encode('utf8')).decode('utf8'),
                json['content'],
                base64.b64decode(json['name'].encode('utf8')).decode('utf8')
            )