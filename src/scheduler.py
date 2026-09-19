import time

from src.messenger import Messenger
from datetime import datetime
from .models.date import Date
from .models.message import Message
from .models.file import File
from .logger import logger
from .writer import writer
from .models.job import Job

class Scheduler:
    def __init__(self):
        self.messenger = Messenger()

    def start(self):
        logger.clear_log()
        logger.log('Starting Scheduler')
        while True:
            time.sleep(60)
            logger.log('Searching for due Jobs')
            job = self.find_job()
            if job:
                self.send_message(job)
            else:
                logger.log('No jobs found')

    def find_job(self):
        today = Date(datetime.today().year, datetime.today().month, datetime.today().day, datetime.today().hour, datetime.today().minute)
        jobs: list[Job] = writer.parse_jobs()
        for job in jobs:
            if job.due_date.before(today):
                logger.log('Active Job found')
                logger.log('Deleting Job with line_number: ' + str(job.line_number))
                writer.delete_job(job.line_number)
                return job
        return None

    def send_message(self, job: Job):
        logger.log('Sending Message')
        self.messenger.set_contacts(job.contacts)
        self.messenger.set_message(job.message)
        self.messenger.set_file(job.file)
        self.messenger.send_message('logger')
        self.messenger.set_contacts(None)
        self.messenger.set_message(Message())
        self.messenger.set_file(File())
        logger.log('Message sent')