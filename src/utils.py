from sys import platform
from src import contacts
from src import message
import questionary
import os


def clear_terminal():
    if platform == "win32":
        os.system('cls')
    elif platform == "linux" or platform == "linux2":
        os.system('clear')

def single_action_menu(title, functions):
    functions.update({"exit": lambda: print("schließe " + title)})
    user_input = None
    while user_input != "exit":
        clear_terminal()
        user_input = questionary.select(
                 "<--- " + title + " --->",
                 choices = functions.keys()
                ).ask()
        functions[user_input]()

def send_message_menu(**kwargs):
    single_action_menu("Nachricht senden", {
            "Kontakte auswählen": lambda: kwargs.update({'contacts': select_contacts_menu()}),
            "Kontakte anzeigen": lambda: contacts.display_contacts(kwargs.get('contacts')),
            "Bild auswählen": lambda: kwargs.update({'picture_path': questionary.path("Pfad: ").ask()}),
            "Bild-Pfad anzeigen:": lambda: display(kwargs.get('picture_path')),
            "Dokument auswählen": lambda: kwargs.update({'document_path': questionary.path("Pfad: ").ask()}),
            "Dokument-Pfad anzeigen:": lambda: display(kwargs.get('document_path')),
            "Nachricht auswählen": lambda: kwargs.update({'message_path': questionary.path("Pfad: ").ask()}),
            "Nachricht anzeigen": lambda: message.display_message(kwargs.get('message_path')),
            "Nachricht abschicken": lambda: message.send_message(kwargs.get('contacts'), kwargs.get('message_path'), kwargs.get('picture_path'), kwargs.get('document_path'))
        })

def select_contacts_menu(**kwargs):
    single_action_menu("Gruppe auswählen", {
            "Alle": lambda: kwargs.update({'contacts': contacts.select_contacts("all")}),
            "Mitglieder": lambda: kwargs.update({'contacts': contacts.select_contacts("mitglied")}),
            "Interessierte": lambda: kwargs.update({'contacts': contacts.select_contacts("interessiert")}),
            "Lernnetz": lambda: kwargs.update({'contacts': contacts.select_contacts("lernnetz")}),
        })
    return kwargs.get('contacts')

def display(text):
    user_input = None
    while user_input != 'q':
        print(text)
        user_input = input("Press q to quit: ")


def plan_message_menu():
    pass