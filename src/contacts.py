from collections import namedtuple
from sys import platform

from selenium.webdriver.common.devtools.v85.indexed_db import ObjectStore

from src import utils
import questionary
import csv
import os

from src.utils import display


def select_contacts(status, csv_path="../user-data/contacts.csv"):
    Contact = namedtuple('Contact', [
        'first_name',
        'last_name',
        'email',
        'status',
        'tags',
        'sex'
    ])
    contacts = {}
    if platform == "win32" and csv_path == "../user-data/contacts.csv":
        csv_path = os.getcwd() + "\\user-data\\contacts.csv"
    try:
        with open(csv_path) as data:
            contact_data = csv.reader(data, delimiter=',', quotechar='"')
            next(contact_data)
            for row in contact_data:
                number = utils.assign_phone_number(row[4], row[5])
                tags = utils.assign_tag_list(row[6])
                state = utils.assign_state(tags)
                sex = utils.assign_sex(row[7])
                first_name = str(row[1]).split(" ")[0]
                contacts.update({number: Contact(first_name, row[2], row[3], state, tags, sex)})
                # row[0] ist die Nationbuilder ID und die brauchen wir hier sicher nicht.
    except FileNotFoundError:
        utils.display("Die contacts.csv Datei konnte nicht gefunden werden. Exportiere eine .csv Datei aus dem Nationbuilder")
    else:
        choices = []
        for number in contacts.keys():
            if (str(status) == str(contacts[number].status) or
                    status == "all" or
                    (contacts[number].status not in ["interessiert", "mitglied", "lernnetz"] and
                    str(status) not in ["interessiert", "mitglied", "lernnetz"])):
                choices.append(contacts[number].first_name + " - " + number + " - " + contacts[number].status + " - " + contacts[number].sex)

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
            text += contacts[number].first_name + " " + contacts[number].last_name + " " + number + " " + contacts[number].sex + "\n"
    utils.display(text)
