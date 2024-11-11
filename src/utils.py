from sys import platform
import os
import re

relevant_tags = {
    "JL Mitglied": "mitglied",
    "JL Kontaktformular": "interessiert",
    "JL Kontakt Freundeskreis": "interessiert",
    "JL Mitmachen": "interessiert",
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

def assign_sex(char):
    if char == "m" or char == "M":
        return "Male"
    if char == "f" or char == "F":
        return "Female"
    if char == "o" or char == "O":
        return "Other"
    return "Not known"

def assign_tag_list(tag_list):
    tags = []
    tag = ""
    for char in tag_list:
        if char != ',':
            tag += char
        else:
            tags.append(tag.strip(" "))
            tag = ""
    tags.append(tag.strip(" "))
    return tags

def assign_state(tags):
    tag_set = [tag for tag in tags if tag in relevant_tags.keys() and relevant_tags[tag] == "mitglied"]
    if len(tag_set) != 0:
        return "mitglied"
    tag_set = [tag for tag in tags if tag in relevant_tags.keys() and relevant_tags[tag] == "interessiert"]
    if len(tag_set) != 0:
        return "interessiert"
    return "sonstiges"

def assign_phone_number(phone_number, mobile_number):
    phone_number = assign_number(phone_number)
    mobile_number = assign_number(mobile_number)
    if phone_number == mobile_number:
        return phone_number
    elif phone_number is None or len(phone_number) == 0:
        return mobile_number
    elif mobile_number is None or len(mobile_number) == 0:
        return phone_number
    return None

def assign_number(call_number):
    if call_number is None or len(call_number) == 0:
        return None
    number = ""
    for char in call_number:
        if char.isdigit():
            number += char
    patterns = ["0043[0-9]*", "0[0-9]*", "43[0-9]*", "[^0][0-9]*"]
    i = 0
    while i < len(patterns):
        pattern = re.compile(patterns[i])
        if pattern.match(number):
            if i == 0:
                number = "+" + number[2:]
            elif i == 1:
                number = "+43" + number[1:]
            elif i == 2:
                number = "+" + number
            elif i == 3:
                number = "+43" + number
            return number
        i += 1
    return number