from selenium import webdriver
import os
import time
from sys import platform

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models.contact import Contact
from .models.message import Message
from .models.file import File

class Driver:
    X_PATHS = {
        "new_chat": "//*[@type='button' and @aria-label='Neuer Chat']",
        "search_field": "//*[@role='textbox']",
        "first_item": "//*[@role='listitem' and @data-testid='list-item-0']",
        "message_field": "//*[@data-testid='conversation-compose-box-input']",
        "description_field": "//*[@data-testid='media-caption-input-container']",
    }

    def __init__(self):
        options = webdriver.ChromeOptions()
        path_option = str("user-data-dir=" + os.getcwd() + "/session-data")
        if platform == "win32":
            path_option = str("user-data-dir=" + os.getcwd() + "\\\\session-data")
        options.add_argument(path_option)
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "disable-popup-blocking"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com")
        self.wait = WebDriverWait(self.driver, 30)

    def openChat(self, contact: Contact):
        try:
            new_chat = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["new_chat"])))
            new_chat.click()
        except:
            raise Exception("XPath für neuen Chat ist inkorrekt")
        else:
            try:
                search_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["search_field"])))
                search_field.click()
                search_field.clear()
            except:
                raise Exception("XPath für das Suchfeld ist inkorrekt")
            else:
                for c in contact.getPhoneNumber():
                    search_field.send_keys(c)
                time.sleep(1)
                try:
                    first_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["first_item"])))
                    first_item.click()
                except:
                    self.driver.get("https://web.whatsapp.com")
                    raise TimeoutException

    def send_file(self, file: File):
        JAVA_SCRIPT = """
            const messageField = arguments[0];
            const type = arguments[1];
            const content = arguments[2];
            const name = arguments[3];
            const response = await fetch(`data:${type};base64,${content}`);
            const blob = await response.blob();
            const file = new File([blob], name, {type: blob.type});
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            const event = new ClipboardEvent('paste', {
                clipboardData: dataTransfer,
                bubbles: true
            });
            messageField.dispatchEvent(event);
        """
        try:
            message_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["message_field"])))
            self.driver.execute_script(JAVA_SCRIPT, message_field, file.get_type(), file.get_content(), file.get_name())
        except:
            raise Exception("XPath für das Message Feld ist inkorrekt")

    def sendEmojie(self, input_field, unicode_character: str):
        JAVA_SCRIPT = """
            const inputField = arguments[0];
            const message = arguments[1];
            const dataTransfer = new DataTransfer();
            dataTransfer.setData('text', message);
            const event = new ClipboardEvent('paste', {
                clipboardData: dataTransfer,
                bubbles: true
            });
            inputField.dispatchEvent(event);
        """
        self.driver.execute_script(JAVA_SCRIPT, input_field, unicode_character)

    def writeMessage(self, message: Message):
        try:
            message_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["message_field"])))
            message_field.click()
        except:
            raise Exception("XPath für das Message Feld ist inkorrekt")
        else:
            for c in message.get_message():
                if int(c.encode().hex(), 16) == 0x000A:
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                elif int(c.encode().hex(), 16) <= 0xFFFF:
                    message_field.send_keys(c)
                else:
                    self.sendEmojie(message_field, c)
            message_field.send_keys(Keys.ENTER)

    def writeDescription(self, message: Message):
        try:
            description_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["description_field"])))
            description_field.click()
        except:
            raise Exception("XPATH für das Description Feld ist inkorrekt")
        else:
            for c in message.get_message():
                if int(c.encode().hex(), 16) == 0x000A:
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                elif int(c.encode().hex(), 16) <= 0xFFFF:
                    description_field.send_keys(c)
                else:
                    self.sendEmojie(description_field, c)
            description_field.send_keys(Keys.ENTER)