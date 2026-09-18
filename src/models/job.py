from typing import List

from .date import Date
from .message import Message
from .contact import Contact
from .file import File

class Job:
    def __init__(self, line_number, due_date, message, contacts, file):
        self.line_number: int = line_number
        self.due_date: Date = due_date
        self.message: Message = message
        self.contacts: List[Contact] = contacts
        self.file: File = file