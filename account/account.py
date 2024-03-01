from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.balance = balance

    def __repr__(self):
        return f"Name: {self.name} Balance: {self.balance}"

    def deposit(self, amount):
        if amount <= Decimal(0.00):
            raise ValueError("amount cannot be less than 0")
        self.balance += amount


a11 = Account('A', Decimal(10))
print(a11)
# print(a1.balance)
# a1.balance = 1000
# print(a1.balance)

