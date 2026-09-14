from selenium.common import TimeoutException

from .models.file import File
from .models.message import Message
from .models.date import Date
from .driver import Driver
from .reader import CSVReader

import time


class Messenger:
    def __init__(self):
        self.driver = Driver()
        self.reader = CSVReader()
        self.message = Message()
        self.file = File()
        self.date = Date()
        self.contacts = None
        self.isBusy = False

    def set_isBusy(self, isBusy):
        self.isBusy = isBusy

    def set_contacts(self, contacts):
        self.contacts = contacts

    def set_file(self, file):
        self.file = file

    def set_message(self, message):
        self.message = message

    def is_Busy(self):
        if self.isBusy:
            self.display("Messenger is Busy try again later.")
            return True
        else:
            self.isBusy = True
            return False

    def display(self, text: str):
        user_input = None
        while user_input != 'q':
            print(text)
            user_input = input("Press q to quit: ")

    def select_csv_file(self):
        if not self.is_Busy():
            self.reader.select_file()
            self.isBusy = False

    def display_csv_path(self):
        if not self.is_Busy():
            self.display(self.reader.get_file_path())
            self.isBusy = False

    def select_contacts(self):
        if not self.is_Busy():
            self.contacts = self.reader.select_contacts()
            self.isBusy = False

    def display_contacts(self):
        if not self.is_Busy():
            if self.contacts is None:
                self.display('None')
            else:
                user_input = None
                while user_input != 'q':
                    for contact in self.contacts:
                        print(contact)
                    user_input = input('Press q to quit: ')
            self.isBusy = False

    def select_file(self):
        if not self.is_Busy():
            self.file.select_file()
            self.isBusy = False

    def display_file_path(self):
        if not self.is_Busy():
            self.display(self.file.get_path())
            self.isBusy = False

    def select_message(self):
        if not self.is_Busy():
            self.message.select_message()
            self.isBusy = False

    def display_message(self):
        if not self.is_Busy():
            user_input = None
            while user_input != 'q':
                print(self.message.get_message())
                user_input = input("Press q to quit: ")
            self.isBusy = False

    def select_date(self):
        if not self.is_Busy():
            self.date.select_date()
            self.isBusy = False

    # Diese Methode soll prüfen ob alles Notwendige da ist, also
    # Nachricht, Kontakte, Datei und Uhrzeit
    # Und soll das dann in eine passende JOBS CSV schreiben.
    # Danach wird alles wieder auf die Anfangswerte gesetzt.
    def schedule_message(self):
        if not self.is_Busy():
            self.contacts = None
            self.file = File()
            self.message = Message()
            self.date = Date()
            self.isBusy = False

    def send_message(self):
        if not self.is_Busy():
            if not self.message is None:
                for contact in self.contacts:
                    print(contact, end=" ", flush=True)
                    self.message.insert_receiver(contact)
                    try:
                        self.driver.openChat(contact)
                    except TimeoutException as exception:
                        print("X (NoWhatsApp)")
                        continue
                    except Exception as exception:
                        print(str(exception))
                        break
                    else:
                        try:
                            if self.file.get_path() is not None:
                                self.driver.send_file(self.file)
                                self.driver.writeDescription(self.message)
                            else:
                                self.driver.writeMessage(self.message)
                            print("\U0001F44D")
                            time.sleep(2)
                        except Exception as exception:
                            print(str(exception))
                            break
                self.file.reset()
                self.display("Done")
            self.isBusy = False