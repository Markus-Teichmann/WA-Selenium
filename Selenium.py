from src.web_interface import WebInterface
from selenium import webdriver
from sys import platform
from src import utils
import questionary
import time
import os

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    if platform == "linux" or platform == "linux2":
        options.add_argument(r"user-data-dir=./session-data/")
    elif platform == "win32":
        path_option = str("user-data-dir=" + os.getcwd() + "\\\\session-data")
        options.add_argument(path_option)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    WebInterface(webdriver.Chrome(options=options))

    WebInterface.driver.maximize_window()
    WebInterface.driver.get('https://web.whatsapp.com')

    utils.single_action_menu("Hauptmenü", {
            "Nachricht verschicken": utils.send_message_menu,
            "Nachricht planen": utils.plan_message_menu,
        })
    WebInterface.driver.close()
