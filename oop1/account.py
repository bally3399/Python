from oop1.exceptions import InvalidAmountException, InvalidPinException, InsufficientFundsException


class Account:
    def __init__(self, name, pin, number):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.number = number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def get_number(self):
        return self.number

    def deposit(self, amount):
        if not amount > 0:
            raise InvalidAmountException("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount, pin):
        if not self.pin == pin:
            raise InvalidPinException("Invalid pin")
        if not 0 < amount <= self.balance:
            raise InsufficientFundsException("Insufficient Balance or invalid amount")
        self.balance -= amount

    def check_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise InvalidPinException("Enter valid pin")
