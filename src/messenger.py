from .models.file import File
from .models.message import Message
from .driver import Driver
from .reader import CSVReader


class Messenger:
    def __init__(self):
        self.driver = Driver()
        self.reader = CSVReader()
        self.message = Message()
        self.file = File()
        self.contacts = None

    def select_csv_file(self):
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

    def send_message(self):
        if not self.message is None:
            for contact in self.contacts:
                print(contact, end=" ")
                self.message.insert_receiver(contact)
                self.driver.openChat(contact)
                if self.file.get_path() is not None:
                    self.driver.send_file(self.file)
                    self.driver.writeDescription(self.message)
                else:
                    self.driver.writeMessage(self.message)
                print("\U0001F44D")
            self.file.reset()