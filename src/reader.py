import csv
import os
import questionary

from .models.contact import Contact
from sys import platform

class CSVReader:
    def __init__(self):
        if platform == "win32":
            self.path = os.getcwd() + "\\user-data\\contacts.csv"
        else:
            self.path = '../user-data/contacts.csv'

    def get_file_path(self):
        return self.path

    def select_file(self):
        file = questionary.path("Pfad").ask()
        self.path = os.path.abspath(file)

    def select_contacts(self):
        if not os.path.exists(self.path):
            return None
        contacts = {}
        with open(self.path, encoding="utf-8") as data:
            file = csv.reader(data, delimiter=",")
            next(file)
            for line in file:
                if line[3] != "":
                    contacts.update({
                        line[1] + " - " + line[2] + " - " + line[3]:
                        Contact(line[1], line[2], line[3])
                    })
        contacts = dict(sorted(contacts.items()))
        keys = questionary.checkbox(
            "Kontakte auswählen: ",
            choices = contacts.keys()
        ).ask()
        selection = []
        for key in keys:
            selection.append(contacts[key])
        return selection