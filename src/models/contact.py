class Contact:
    def __init__(self, first_name=None, last_name=None, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def getFirstName(self):
        return self.first_name

    def getPhoneNumber(self):
        return self.phone_number

    def serialize(self):
        if self is None or self.first_name is None or self.last_name is None or self.phone_number is None:
            return None
        return ('{' +
                '\"first_name\": \"' + self.first_name + '\", ' +
                '\"last_name\": \"' + self.last_name + '\", ' +
                '\"phone_number\": \"' + self.phone_number +
        '\"}')

    def __str__(self):
        return self.first_name + " - " + self.last_name + " - " + self.phone_number