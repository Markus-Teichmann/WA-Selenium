from .contact import Contact
import questionary
import os


class Message:
    def __init__(self):
        self.path = None
        self.message = None

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