from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains
from collections import namedtuple 
from sys import platform
import questionary
import time
import re
import os

specials = {
        "linebreak": lambda: ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform(), 
        "tab": lambda: ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform(),
        "enter": lambda: ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform(),
        "Strg-A": lambda: ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        }
        
JS_DROP_FILE = """
	var target = arguments[0],
		offsetX = arguments[1],
		offsetY = arguments[2],
		document = target.ownerDocument || document,
		window = document.defaultView || window;

	var input = document.createElement('INPUT');
	input.type = 'file';
	input.onchange = function () {
		var rect = target.getBoundingClientRect(),
			x = rect.left + (offsetX || (rect.width >> 1)),
			y = rect.top + (offsetY || (rect.height >> 1)),
			dataTransfer = { files: this.files };

		['dragenter', 'dragover', 'drop'].forEach(function (name) {
			var evt = document.createEvent('MouseEvent');
			evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
			evt.dataTransfer = dataTransfer;
			target.dispatchEvent(evt);
		});

		setTimeout(function () { document.body.removeChild(input); }, 25);
	};
	document.body.appendChild(input);
	return input;
"""

def get_search_field():
    return driver.find_element(By.XPATH, "//*[@tabindex='3']")

def open_chat(number):
    search_field = get_search_field()
    #specials["Strg-A"]()
    search_field.send_keys(number)
    search_field.send_keys(Keys.ENTER)
    time.sleep(0.2)

#Nur dann ausführen, wenn wir bereits einen Chat geöffnet haben.
def get_message_field():
    return driver.find_element(By.XPATH, "//*[@tabindex='10']")

#Nur dann ausführen, wenn wir bereits einen Chat geöffnet haben.
def open_append():
    append_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span")
    append_button.click()
    time.sleep(0.1)

#Nur dann ausführen, wenn wir bereits einen Chat und Anhängen geöffnet haben.
def get_picture_upload_field():
    upload_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input")
    return upload_field

#Nur dann aufrufen, wenn wir bereits ein Bild angehängt haben.
def get_picture_description_field():
    description_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]")
    return description_field

# In dieser Methode werden alle im Text mit $ gekennzeichneten
# Variablen durch die in der Methode write_message definierten Inhalte
# ersetzt.
def replace_variables(line, variables):
    line = line.replace("\r", "").replace("\n", "")
    for variable in variables.keys():
        line = line.replace(variable, variables[variable])
    return line

# Diese Methode erstzt alle mit \emoji\ gekennzeichneten Emojis durch für
# WhatsApp verstänliche :emoji kennzeichen. Diese lassen sich dann mit
# der Tab taste vervollständigen.
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
    message = open(message_path)
    for line in message:
        line = replace_variables(line, variables)
        line_parts = replace_emojis(line)
        index = 0 
        while index < len(line_parts["emojis"]):
            message_field.send_keys(line_parts["text"][index])
            message_field.send_keys(line_parts["emojis"][index])
            time.sleep(0.5)
            specials["tab"]()
            index += 1
        message_field.send_keys(line_parts["text"][-1])
        specials["linebreak"]()

# Diese Methode verschickt die angegebene Nachricht an jeden in
# contacts hinterlegten Kontakt.
def send_message(contacts, message_path=None, picture_path=None):
    for number in contacts.keys():
        variables = { "$name": contacts[number].name, "$number": number }
        open_chat(number)
        message_field = get_message_field()
        if picture_path is not None:
            open_append()
            picture_upload = get_picture_upload_field()
            picture_path = os.path.abspath(picture_path)
            picture_upload.send_keys(picture_path)
            time.sleep(20)
            message_field = get_picture_description_field()
        if message_path is not None:
            write_message(variables, message_path, message_field)
        time.sleep(2)
        specials["enter"]()
        time.sleep(2)

def single_action_menu(title, functions):
    functions.update({"exit": lambda: print("schließe " + title)})
    user_input = None
    while user_input != "exit":
        clear_terminal()
        user_input = questionary.select(
                 "<--- " + title + " --->",
                 choices = functions.keys()
                ).ask()
        functions[user_input]()

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def send_message_menu(**kwargs):
    single_action_menu("Nachricht senden", {
            "Kontakte auswählen": lambda: kwargs.update({'contacts': select_contacts("all")}),
            "Kontakte anzeigen": lambda: display_contacts(kwargs.get('contacts')),
            "Bild auswählen": lambda: kwargs.update({'picture_path': select_picture()}),
            "Nachricht auswählen": lambda: kwargs.update({'message_path': select_message_path()}),
            "Nachricht anzeigen": lambda: display_message(kwargs.get('message_path')),
            "Nachricht abschicken": lambda: send_message(kwargs.get('contacts'), kwargs.get('message_path'), kwargs.get('picture_path'))
        })

def select_contacts(which):
    Contact = namedtuple('Contact', ['name', 'status'])
    contacts = {
    			#ToDo Daten einfügen:
				"+43123456789": Contact("Name", "Status")
            }
    choices = []
    for number in contacts.keys():
        if which == contacts[number].status or which == "all":
            choices.append(contacts[number].name + " - " + number)
    selection_keys = questionary.checkbox(
                "Kontakte auswählen: ",
                choices = choices
            ).ask()
    selection = {}
    for key in selection_keys:
        number = key.split(" - ", 1)[1]
        selection.update({number: contacts.get(number)})
    return selection

def display_contacts(contacts):
    text = ""
    for number in contacts.keys():
        text += contacts[number].name + " " + number + "\n"
    display(text)

def select_picture():
    return questionary.path("Pfad: ").ask()

def select_message_path(**kwargs):
    single_action_menu("Nachricht angeben", {
            "Neue Nachricht schreiben": lambda: print("ToDo"),
            "Pfad zur Nachricht angeben": lambda: kwargs.update({'message_path': questionary.path("Pfad: ").ask()})
        })
    return kwargs.get('message_path')

def display_message(message_path):
    if message_path is not None:
        message = open(message_path)
        display(message.read())

def display(text):
    user_input = None
    while user_input != 'q':
        print(text)
        user_input = input("Press q to quit: ")

def plan_message_menu():
    print("Still a ToDo")

def edit_contacts():
    pass

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    if platform == "linux" or platform == "linux2":
        options.add_argument(r"user-data-dir=./data")
    elif platform == "win32":
        path_option = str("user-data-dir=" + os.getcwd() + "\\\\data")
        options.add_argument(path_option)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get('https://web.whatsapp.com')

    single_action_menu("Hauptmenü", {
            "Nachricht verschicken": send_message_menu,
            "Nachricht planen": plan_message_menu,
        })
    driver.close()
