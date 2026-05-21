import time

from .models.image import Image
from .models.document import Document
from .models.message import Message
from .driver import Driver
from .reader import CSVReader


class Messenger:
    def __init__(self):
        self.driver = Driver()
        self.reader = CSVReader()
        self.message = Message()
        self.document = Document()
        self.image = Image()
        self.contacts = None

    def select_file(self):
        self.reader.select_file()

    def display(self, text: str):
        user_input = None
        while user_input != 'q':
            print(text)
            user_input = input("Press q to quit: ")

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

    def select_image(self):
        self.image.select_image()

    def display_image_path(self):
        self.display(self.image.get_path())

    def select_document(self):
        self.document.select_document()

    def display_document_path(self):
        self.display(self.document.get_path())

    def move_document(self):
        self.document.move_to_clipboard()

    def select_message(self):
        self.message.select_message()

    def display_message(self):
        user_input = None
        while user_input != 'q':
            print(self.message.get_message())
            user_input = input("Press q to quit: ")

    def send_message(self):
        if not self.message is None:
            #if self.image.get_path() is not None:
            #    self.image.move_to_clipboard()
            #elif self.document.get_path() is not None:
            #    self.document.move_to_clipboard()
            for contact in self.contacts:
                print(contact, end=" ")
                self.message.insert_receiver(contact)
                self.driver.openChat(contact)
                if self.image.get_path() is not None:
                    self.image.move_to_clipboard()
                    time.sleep(3)
                    self.driver.paste()
                    self.driver.writeDescription(self.message)
                elif self.document.get_path() is not None:
                    self.document.move_to_clipboard()
                    time.sleep(3)
                    self.driver.paste()
                    self.driver.writeDescription(self.message)
                else:
                    time.sleep(1)
                    self.driver.writeMessage(self.message)
                print("\U0001F44D")
            self.image.reset()
            self.document.reset()
