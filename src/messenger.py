from typing import Callable

from selenium.common import TimeoutException

from .models.file import File
from .models.message import Message
from .models.date import Date
from .driver import driver
from .reader import CSVReader

import time
import os


class Messenger:
    def __init__(self):
        self.reader = CSVReader()
        self.message = Message()
        self.file = File()
        self.date = Date()
        self.contacts = None

    def set_contacts(self, contacts):
        self.contacts = contacts

    def set_file(self, file):
        self.file = file

    def set_message(self, message):
        self.message = message

    def display(self, text: str):
        user_input = None
        while user_input != 'q':
            print(text)
            user_input = input("Press q to quit: ")

    def select_csv_file(self):
        self.reader.select_file()

    def display_csv_path(self):
        self.display(self.reader.get_file_path())

    def select_contacts(self):
        self.contacts = self.reader.select_contacts()

    def display_contacts(self):
        if self.contacts is None:
            self.display('None')
        else:
            user_input = None
            while user_input != 'q':
                for contact in self.contacts:
                    print(contact)
                user_input = input('Press q to quit: ')

    def select_file(self):
        self.file.select_file()

    def display_file_path(self):
        self.display(self.file.get_path())

    def select_message(self):
        self.message.select_message()

    def display_message(self):
        user_input = None
        while user_input != 'q':
            print(self.message.get_message())
            user_input = input("Press q to quit: ")

    def select_date(self):
        self.date.select_date()

    # Diese Methode soll prüfen, ob alles Notwendige da ist, also
    # Nachricht, Kontakte, Datei und Uhrzeit
    # Und soll das dann in eine passende JOBS CSV schreiben.
    # Danach wird alles wieder auf die Anfangswerte gesetzt.
    def schedule_message(self):
        self.select_date()
        date = self.date.serialize()
        message = self.message.serialize()
        contacts = '['
        for i in range(len(self.contacts) -1):
            contact = self.contacts[i]
            contacts += contact.serialize() + ', '
        contact = self.contacts[len(self.contacts) - 1]
        contacts += contact.serialize() + ']'
        file = self.file.serialize()
        if date is None or message is None or len(self.contacts) == 0:
            print("Bitte gebe zumindest ein Datum, eine Nachricht und Kontakte an.")
            time.sleep(3)
        else:
            json = ('{' +
                '\"date\": ' + date + ', ' +
                '\"message\": ' + message + ', ' +
                '\"contacts\": ' + contacts + ', ' +
                '\"file\": ' + file +
            '}')
            file_path = os.path.abspath('./user-data/jobs.CSV')
            file_size = os.path.getsize(file_path)
            with open(file_path, 'a', encoding='utf-8') as file:
                if file_size == 0:
                    file.write(json)
                else:
                    file.write('; ' + json)
        #self.contacts = None
        #self.file = File()
        #self.message = Message()
        #self.date = Date()

    def send_message(self):
        if not self.message is None and not self.contacts is None:
            driver.send_message_thread_safe(self.contacts, self.message, self.file)
        #if not self.message is None:
        #    for contact in self.contacts:
        #        print(contact, end=" ", flush=True)
        #        self.message.insert_receiver(contact)
        #        try:
        #            self.driver.openChat(contact)
        #        except TimeoutException as exception:
        #            print("X (NoWhatsApp)")
        #            continue
        #        except Exception as exception:
        #            print(str(exception))
        #            break
        #        else:
        #            try:
        #                if self.file.get_path() is not None:
        #                    self.driver.send_file(self.file)
        #                    self.driver.writeDescription(self.message)
        #                else:
        #                    self.driver.writeMessage(self.message)
        #                print("\U0001F44D")
        #                time.sleep(2)
        #            except Exception as exception:
        #                print(str(exception))
        #                break
        #    self.file.reset()
        #    self.display("Done")

    #def test_driver(self):
    #    driver.test()