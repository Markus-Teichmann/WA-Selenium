import os
import time
from typing import Callable
from datetime import datetime

class Logger:
    def __init__(self, path):
        self.is_busy = False
        self.path = os.path.abspath(path)

    def __thread_safe(self, function: Callable):
        if self.is_busy:
            return False
        else:
            self.is_busy = True
            function()
            self.is_busy = False
            return True

    def __wait_for(self, function: Callable):
        while not self.__thread_safe(function):
            time.sleep(1)

    def __log(self, message: str):
        day = str(datetime.today().day)
        month = str(datetime.today().month)
        year = str(datetime.today().year)
        hour = str(datetime.today().hour)
        minute = str(datetime.today().minute)
        seconds = str(datetime.today().second)
        with open(self.path, "a") as file:
            file.write('[' + day + '-' + month + '-' + year + ' ' + hour + ':' + minute + ':' + seconds + '] ' + message + "\n")

    def __clear_log(self):
        with open(self.path, "w") as file:
            file.close()

    def log(self, message:str):
        self.__wait_for(lambda: self.__log(message))

    def clear_log(self):
        self.__wait_for(lambda: self.__clear_log())

logger = Logger('./user-data/log.log')
