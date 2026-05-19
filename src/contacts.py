from collections import namedtuple
from sys import platform

from src import utils
import questionary
import csv
import os


def select_contacts(status, csv_path="../user-data/contacts.csv"):
    Contact = namedtuple('Contact', [
        'first_name',
        'last_name'
    ])
    contacts = {}
    if platform == "win32" and csv_path == "../user-data/contacts.csv":
        csv_path = os.getcwd() + "\\user-data\\contacts.csv"
    try:
        with open(csv_path, encoding="utf8") as data:
            contact_data = csv.reader(data, delimiter=',', quotechar='"')
            next(contact_data)
            for row in contact_data:
                number = utils.assign_phone_number(row[3])
                if number is not None:
                    first_name = str(row[1])
                    last_name = str(row[2])
                    contacts.update({number: Contact(first_name, last_name)})
    except FileNotFoundError:
        utils.display("Die contacts.csv Datei konnte nicht gefunden werden. Exportiere eine .csv Datei aus dem Nationbuilder")
    else:
        choices = []
        for number in contacts.keys():
            choices.append(contacts[number].first_name + " - " + contacts[number].last_name + " - " + number)

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
                number = key.split(" - ")[2]
                selection.update({number: contacts[number]})
            return selection

def display_contacts(contacts):
    text = ""
    if contacts is not None:
        for number in contacts.keys():
            text += contacts[number].first_name + " " + contacts[number].last_name + " " + number + "\n"
    utils.display(text)
