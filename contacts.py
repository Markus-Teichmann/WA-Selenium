from collections import namedtuple
from sys import platform
import questionary
import utils
import csv
import os

def select_contacts(status):
    Contact = namedtuple('Contact', ['name', 'status'])
    contacts = {}
    path = "./user-data/contacts.csv"
    if platform == "win32":
        path = os.getcwd() + "\\\\user-data\\\\contacts.csv"
    with open(path) as data:
        contact_data = csv.reader(data, delimiter=',')
        next(contact_data)
        for row in contact_data:
            contacts.update({row[0]: Contact(row[1], row[2])})
    choices = []
    for number in contacts.keys():
        if str(status) == str(contacts[number].status) or status == "all":
            choices.append(contacts[number].name + " - " + number + " - " + contacts[number].status)
    selection_keys = questionary.checkbox(
                "Kontakte auswählen: ",
                choices = choices
            ).ask()
    selection = {}
    for key in selection_keys:
        number = key.split(" - ", 2)[1]
        selection.update({number: contacts[number]})
    return selection

def display_contacts(contacts):
    text = ""
    for number in contacts.keys():
        text += contacts[number].name + " " + number + "\n"
    utils.display(text)
