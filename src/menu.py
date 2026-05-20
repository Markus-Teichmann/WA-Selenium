from sys import platform
import os
from typing import Callable

import questionary

class Menu:
    def __init__(self, title):
        self.title = title
        self.functions = dict()

    def clear(self):
        if platform == "win32":
            os.system('cls')
        elif platform == "linux" or platform == "linux2":
            os.system('clear')

    def insert_option(self, label: str, function: Callable):
        self.functions.update({label: function})

    def display(self):
        self.functions.update({"exit": lambda: print("schließe " + self.title)})
        self.clear()
        user_input = None
        while user_input != "exit":
            self.clear()
            user_input = questionary.select(
                "<--- " + self.title + " --->",
                choices=self.functions.keys()
            ).ask()
            self.functions[user_input]()