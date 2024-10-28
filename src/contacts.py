from collections import namedtuple
from sys import platform
from src import utils
import questionary
import csv
import os

def select_contacts(status):
    Contact = namedtuple('Contact', ['name', 'status'])
    contacts = {}
    path = "../user-data/contacts.csv"
    if platform == "win32":
        path = os.getcwd() + "\\user-data\\contacts.csv"
    try:
        with open(path) as data:
            contact_data = csv.reader(data, delimiter=',')
            next(contact_data)
            for row in contact_data:
                contacts.update({row[0]: Contact(row[1], row[2])})
    except FileNotFoundError:
        utils.display("Die contacts.csv Datei konnte nicht gefunden werden. Frage nach dem user-data Ordner.")
    else:
        choices = []
        for number in contacts.keys():
            if str(status) == str(contacts[number].status) or status == "all":
                choices.append(contacts[number].name + " - " + number + " - " + contacts[number].status)
        try:
            selection_keys = questionary.checkbox(
                        "Kontakte auswählen: ",
                        choices = choices
                    ).ask()
        except AttributeError:
            utils.display("Es scheint keine Kontakte unter der gegebenen Kategorie zu geben. Überprüfe die .csv Datei.")
        else:
            selection = {}
            for key in selection_keys:
                number = key.split(" - ", 2)[1]
                selection.update({number: contacts[number]})
            return selection

def display_contacts(contacts):
    text = ""
    if contacts is not None:
        for number in contacts.keys():
            text += contacts[number].name + " " + number + "\n"
    utils.display(text)
