import datetime
import re

from typing import Self

class Date:
    def __init__(self, year=None, month=None, day=None, hour=None, minute=None):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def select_date(self):
        valid_date = False
        while not valid_date:
            date = input("Gib das Datum im Format: DD-MM-YYYY an:")
            if None != re.fullmatch('[0-9]{2}-[0-9]{2}-[0-9]{4}', date):
                day = int(date[0:2])
                month = int(date[3:5])
                year = int(date[6:10])
                try:
                    datetime.date(year, month, day)
                except ValueError:
                    valid_date = False
                else:
                    self.year = year
                    self.month = month
                    self.day = day
                    valid_date = True
        valid_time = False
        while not valid_time:
            time = input("Gib die Zeit im Format: HH-MM an:")
            if None != re.fullmatch('[0-9]{2}-[0-9]{2}', time):
                hour = int(time[0:2])
                minute = int(time[3:5])
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    self.hour = hour
                    self.minute = minute
                    valid_time = True

    def before(self, date: Self):
        if int(self.year) > int(date.year):
            return False
        if int(self.year) < int(date.year):
            return True
        if int(self.month) > int(date.month):
            return False
        if int(self.month) < int(date.month):
            return True
        if int(self.day) > int(date.day):
            return False
        if int(self.day) < int(date.day):
            return True
        if int(self.hour) > int(date.hour):
            return False
        if int(self.hour) < int(date.hour):
            return True
        if int(self.minute) > int(date.minute):
            return False
        if int(self.minute) < int(date.minute):
            return True
        return False

    def serialize(self):
        if self is None or self.day is None or self.month is None or self.year is None or self.hour is None or self.minute is None:
            return None
        return ('{' +
            '\"day\": \"' + str(self.day) + '\", ' +
            '\"month\": \"' + str(self.month) + '\", ' +
            '\"year\": \"' + str(self.year) + '\", ' +
            '\"hour\": \"' + str(self.hour) + '\", ' +
            '\"minute\": \"' + str(self.minute) +
        '\"}')

    @staticmethod
    def parse(json: dict):
        if ('day' in json and
            'month' in json and
            'year' in json and
            'hour' in json and
            'minute' in json):
            return Date(json['year'], json['month'], json['day'], json['hour'], json['minute'])