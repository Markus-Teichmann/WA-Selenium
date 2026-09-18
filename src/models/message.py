from .contact import Contact
import questionary
import os
import base64


class Message:
    def __init__(self, path=None, message=None):
        self.path = path
        self.message = message

    def select_message(self):
        self.path = questionary.path("Pfad").ask()
        self.message = open(self.path, 'r', encoding="utf-8").read()

    def insert_receiver(self, contact: Contact):
        if os.path.exists(self.path):
            content = open(self.path, 'r', encoding="utf-8").read()
            self.message = content.replace('$name', contact.first_name)

    def get_message(self):
        return self.message
        #with open(self.message_path,'r', encoding="utf-8") as file:
        #    return file.read().replace('$name', self.to.first_name)

    def serialize(self):
        if self is None or self.path is None or self.message is None:
            return None
        return ('{' +
            '\"path\": \"' + base64.b64encode(self.path.encode('utf8')).decode('utf8') + '\", ' +
            '\"message\": \"' + base64.b64encode(self.message.encode('utf8')).decode('utf8') +
        '\"}')

    @staticmethod
    def parse(json: dict):
        if ('path' in json and
            'message' in json):
            return Message(
                base64.b64decode(json['path'].encode('utf8')).decode('utf8'),
                base64.b64decode(json['message'].encode('utf8')).decode('utf8')
            )