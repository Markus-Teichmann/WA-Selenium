from src import contacts
from src import message
from src import utils
import questionary

def single_action_menu(title, functions):
    functions.update({"exit": lambda: print("schließe " + title)})
    user_input = None
    while user_input != "exit":
        utils.clear_terminal()
        user_input = questionary.select(
                 "<--- " + title + " --->",
                 choices = functions.keys()
                ).ask()
        functions[user_input]()

def send_message_menu(**kwargs):
    single_action_menu("Nachricht senden", {
            "CSV - Datei auswählen": lambda: kwargs.update({'csv_path': questionary.path("Pfad: ").ask()}),
            "CSV-Pfad anzeigen:": lambda: utils.display(kwargs.get('csv_path')),
            "Kontakte auswählen": lambda: kwargs.update({'contacts': select_contacts_menu(kwargs.get('csv_path'))}),
            "Kontakte anzeigen": lambda: contacts.display_contacts(kwargs.get('contacts')),
            "Bild auswählen": lambda: kwargs.update({'picture_path': questionary.path("Pfad: ").ask()}),
            "Bild-Pfad anzeigen:": lambda: utils.display(kwargs.get('picture_path')),
            "Dokument auswählen": lambda: kwargs.update({'document_path': questionary.path("Pfad: ").ask()}),
            "Dokument-Pfad anzeigen:": lambda: utils.display(kwargs.get('document_path')),
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
            "Sonstige": lambda: kwargs.update({'contacts': contacts.select_contacts("sonstige")})
        })
    return kwargs.get('contacts')

def plan_message_menu():
    pass