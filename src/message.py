from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from src.web_interface import WebInterface
from src import utils
import time
import re
import os


specials = {
    "linebreak": lambda: ActionChains(WebInterface.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform(),
    "tab": lambda: ActionChains(WebInterface.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform(),
    "enter": lambda: ActionChains(WebInterface.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform(),
    "Strg-A": lambda: ActionChains(WebInterface.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
}

# In dieser Methode werden alle im Text mit $ gekennzeichneten
# Variablen durch die in der Methode write_message definierten Inhalte
# ersetzt.
def replace_variables(line, variables):
    line = line.replace("\r", "").replace("\n", "")
    for variable in variables.keys():
        line = line.replace(variable, variables[variable])
    return line

# Diese Methode ersetzt alle mit \emoji\ gekennzeichneten Emojis durch für
# WhatsApp verständliche :emoji kennzeichen. Diese lassen sich dann mit
# der Tab-taste vervollständigen.
def replace_emojis(line):
    emojis = re.findall("\\\\[a-z][^\\\\]*[a-z]\\\\", line)
    line_parts = { "text": [], "emojis": [] }
    if len(emojis) != 0:
        text = []
        for emoji in emojis:
            parts = line.split(emoji, 1)
            text.append(parts[0])
            line = parts[1]
        index = 0
        while index < len(emojis):
            line_parts["text"].append(text[index])
            line_parts["emojis"].append(":" + emojis[index][1:-1])
            index += 1
    line_parts["text"].append(line)
    return line_parts

# In dieser Methode wird die angegebene Nachricht Zeile für Zeile an
# das message_field geschickt und wie in der Nachricht spezifiziert
# formatiert.
def write_message(variables, message_path, message_field):
    message = open(message_path, encoding="utf-8")
    for line in message:
        line = replace_variables(line, variables)
        line_parts = replace_emojis(line)
        index = 0
        while index < len(line_parts["emojis"]):
            message_field.send_keys(line_parts["text"][index])
            message_field.send_keys(line_parts["emojis"][index])
            time.sleep(1)
            specials["tab"]()
            index += 1
        message_field.send_keys(line_parts["text"][-1])
        specials["linebreak"]()
        time.sleep(0.5)

# Diese Methode verschickt die angegebene Nachricht an jeden in
# contacts hinterlegten Kontakt.
def send_message(contacts, message_path=None, picture_path=None, document_path=None):
    for number in contacts.keys():
        print(contacts[number].name + " - " + number)
        variables = { "$name": contacts[number].name, "$number": number }
        WebInterface.open_chat(number)
        message_field = WebInterface.get_message_field()
        if picture_path is not None:
            WebInterface.open_append()
            picture_upload = WebInterface.get_picture_upload_field()
            picture_path = os.path.abspath(picture_path)
            picture_upload.send_keys(picture_path)
            time.sleep(20)
            message_field = WebInterface.get_description_field()
        if document_path is not None:
            WebInterface.open_append()
            document_upload = WebInterface.get_document_upload_field()
            document_path = os.path.abspath(document_path)
            document_upload.send_keys(document_path)
            time.sleep(5)
            message_field = WebInterface.get_description_field()
        if message_path is not None:
            write_message(variables, message_path, message_field)
        time.sleep(2)
        specials["enter"]()
        time.sleep(5)
        print("\U0001F44D")

def display_message(message_path):
    if message_path is not None:
        message = open(message_path, encoding="utf-8")
        utils.display(message.read())

