from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

xpaths = {
        "search_field": "//*[@tabindex='3']",
        "message_field": "//*[@tabindex='10']",
        "append_button": "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[1]/div/button/span",
        "picture_upload_field": "/html/body/div[1]/div/div/span[5]/div/ul/div/div/div[2]/li/div/input",
        "document_upload_field": "/html/body/div[1]/div/div/span[5]/div/ul/div/div/div[1]/li/div/input",
        "description_field": "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p"
    }

class WebInterface:

    driver = None
    def __init__(self, driver=None):
        if WebInterface.driver is None:
            WebInterface.driver = driver

    @staticmethod
    def open_chat(number):
        search_field = WebInterface.get_search_field()
        search_field.send_keys(number)
        search_field.send_keys(Keys.ENTER)
        time.sleep(0.2)

    #Nur dann ausführen, wenn wir bereits einen Chat geöffnet haben.
    @staticmethod
    def open_append():
        try:
            append_button = WebInterface.driver.find_element(By.XPATH, xpaths["append_button"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für den Anhang ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für den Anhang ist fehlerhaft.")
        else:
            append_button.click()
            time.sleep(0.1)

    @staticmethod
    def get_search_field():
        try:
            return WebInterface.driver.find_element(By.XPATH, xpaths["search_field"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für das Suchfeld ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für das Suchfeld ist fehlerhaft.")

    #Nur dann ausführen, wenn wir bereits einen Chat geöffnet haben.
    @staticmethod
    def get_message_field():
        try:
            return WebInterface.driver.find_element(By.XPATH, xpaths["message_field"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für das Nachrichtenfeld ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für das Nachrichtenfeld ist fehlerhaft.")

    #Nur dann ausführen, wenn wir bereits einen Chat und Anhängen geöffnet haben.
    @staticmethod
    def get_picture_upload_field():
        try:
            return WebInterface.driver.find_element(By.XPATH, xpaths["picture_upload_field"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für die Bildauswahl ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für die Bildauswahl ist fehlerhaft.")

    #Nur dann ausführen, wenn wir bereits einen Chat und Anhänge geöffnet haben.
    @staticmethod
    def get_document_upload_field():
        try:
            return WebInterface.driver.find_element(By.XPATH, xpaths["document_upload_field"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für die Dokumentauswahl ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für die Dokumentauswahl ist fehlerhaft.")

    #Nur dann aufrufen, wenn wir bereits ein Bild angehängt haben.
    @staticmethod
    def get_description_field():
        try:
            return WebInterface.driver.find_element(By.XPATH, xpaths["description_field"])
        except InvalidSelectorException:
            raise Exception("Der angegebene XPath für das Beschreibungsfeld ist fehlerhaft.")
        except NoSuchElementException:
            raise Exception("Der angegebene XPath für das Beschreibungsfeld ist fehlerhaft.")
