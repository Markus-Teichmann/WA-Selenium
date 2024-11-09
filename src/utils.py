from sys import platform
import os

relevant_tags = {
    "JL Mitglied": "mitglied",
    "JL Kontaktformular": "interessiert",
    "JL Kontakt Freundeskreis": "interessiert",
    "JL Lernnetz": "lernnetz"
}

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

def assign_state(tag_list):
    tag = None
    set = [tag for tag in tag_list if tag in relevant_tags.keys() and relevant_tags[tag] == "mitglied"]
    if len(set) != 0:
        return "mitglied"
    set = [tag for tag in tag_list if tag in relevant_tags.keys() and relevant_tags[tag] == "interessiert"]
    if len(set) != 0:
        return "interessiert"
    return "sonstiges"

def assign_phone_number(phone_number, mobile_number):
    phone_number = assign_number(phone_number)
    mobile_number = assign_number(mobile_number)
    if phone_number == mobile_number:
        return phone_number
    elif phone_number == None or len(phone_number) == 0:
        return mobile_number
    elif mobile_number == None or len(mobile_number) == 0:
        return phone_number
    return None

def assign_number(call_number):
    if call_number == None or len(call_number) == 0:
        return None
    
