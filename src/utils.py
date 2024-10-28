from sys import platform
import os

def clear_terminal():
    if platform == "win32":
        os.system('cls')
    elif platform == "linux" or platform == "linux2":
        os.system('clear')

def display(text):
    user_input = None
    while user_input != 'q':
        print(text)
        user_input = input("Press q to quit: ")
