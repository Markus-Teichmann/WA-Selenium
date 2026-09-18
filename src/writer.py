import os.path
from typing import Callable
import os.path
import time
import json

from .models.date import Date
from .models.message import Message
from .models.contact import Contact
from .models.file import File
from .models.job import Job

class Writer:
    def __init__(self, path):
        self.is_busy = False
        self.path = os.path.abspath(path)

    def __parse_jobs(self):
        jobs = []
        if os.path.getsize(self.path) != 0:
            with open(self.path, 'r', encoding='utf-8') as file:
                job_dto = {
                    "line_number": 0,
                    "due_date": None,
                    "message": None,
                    "contacts": None,
                    "file": None
                }
                for line in file:
                    job_dto["line_number"] += 1
                    line = line.strip('\n')
                    obj = json.loads(line)
                    if 'date' in obj:
                        job_dto['due_date'] = Date.parse(obj['date'])
                    if 'message' in obj:
                        job_dto['message'] = Message.parse(obj['message'])
                    if 'contacts' in obj:
                        contacts = []
                        for contact in obj['contacts']:
                            contact = Contact.parse(contact)
                            contacts.append(contact)
                        job_dto['contacts'] = contacts
                    if 'file' in obj:
                        job_dto['file'] = File.parse(obj['file'])
                    job = Job(job_dto['line_number'], job_dto['due_date'], job_dto['message'], job_dto['contacts'], job_dto['file'])
                    jobs.append(job)
        return jobs


    def __delete_job(self, line_number: int):
        with open(self.path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        line_count = 0
        with open(self.path, 'w', encoding='utf-8') as file:
            for line in lines:
                line_count += 1
                if line_count != line_number:
                    file.write(line)

    def __thread_safe(self, function: Callable):
        if self.is_busy:
            return False
        else:
            self.is_busy = True
            value = function()
            self.is_busy = False
            if value is not None:
                return value
            return True

    def __wait_for(self, function: Callable):
        value = None
        while not value:
            value = self.__thread_safe(function)
            time.sleep(1)
        return value

    def delete_job(self, line_number: int):
        self.__wait_for(lambda: self.__delete_job(line_number))

    def parse_jobs(self):
        return self.__wait_for(lambda: self.__parse_jobs())

writer = Writer('./user-data/jobs.CSV')