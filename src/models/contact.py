class Contact:
    def __init__(self, first_name=None, last_name=None, phone_number=None, membership=None, sex=None, organisation=None, birthday=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.membership = membership
        self.sex = sex
        self.organisation = organisation
        self.birthday = birthday

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
                '\"phone_number\": \"' + self.phone_number + '\", ' +
                '\"membership\": \"' + self.membership + '\", ' +
                '\"sex\": \"' + self.sex +
        '\"}')

    @staticmethod
    def parse(json: dict):
        if ('first_name' in json and
            'last_name' in json and
            'phone_number' in json and
            'membership' in json and
            'sex' in json):
            return Contact(json['first_name'], json['last_name'], json['phone_number'], json['membership'], json['sex'])

    def __str__(self):
        return self.first_name + " - " + self.last_name + " - " + self.phone_number + " - " + self.membership + ' - ' + self.sex