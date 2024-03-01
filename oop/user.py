class User:
    def __init__(self, age, email_address, name, password, phone):
        self.age = age
        self.email_address = email_address
        self.name = name
        self.password = password
        self.phone = phone

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email_address(self):
        return self.email_address

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_phone(self):
        return self.phone
