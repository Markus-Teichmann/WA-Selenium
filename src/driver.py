from selenium import webdriver
import os
import time
from sys import platform
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models.contact import Contact
from .models.message import Message
from .models.file import File

class Driver:
    X_PATHS = {
        "search_field": "//*[@id='_r_9_']",
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
        self.wait = WebDriverWait(self.driver, 60)

    def openChat(self, contact: Contact):
        search_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["search_field"])))
        search_field.click()
        time.sleep(1)
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down('a').key_up('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        for c in contact.getPhoneNumber():
            search_field.send_keys(c)
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(1)

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
        message_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["message_field"])))
        self.driver.execute_script(JAVA_SCRIPT, message_field, file.get_type(), file.get_content(), file.get_name())

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
        message_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["message_field"])))
        message_field.click()
        for c in message.get_message():
            if int(c.encode().hex(), 16) == 0x000A:
                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            elif int(c.encode().hex(), 16) <= 0xFFFF:
                message_field.send_keys(c)
            else:
                self.sendEmojie(message_field, c)
        message_field.send_keys(Keys.ENTER)

    def writeDescription(self, message: Message):
        description_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.X_PATHS["description_field"])))
        description_field.click()
        for c in message.get_message():
            if int(c.encode().hex(), 16) == 0x000A:
                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            elif int(c.encode().hex(), 16) <= 0xFFFF:
                description_field.send_keys(c)
            else:
                self.sendEmojie(description_field, c)
        description_field.send_keys(Keys.ENTER)