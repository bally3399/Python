from oop1.exceptions import AccountNotFoundException, InvalidPinException, InsufficientFundsException
from oop1.account import Account




class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []
        self.counter = 100

    def register_customer(self, first_name: str, last_name: str, pin: str):
        account_number = self.generate_number()
        new_account = Account(first_name + " " + last_name, pin, account_number)
        self.__accounts.append(new_account)

        return new_account

    def generate_number(self):
        self.counter += 1
        return self.counter

    def find_account(self, account_number):
        for account in self.__accounts:
            if account.number == account_number:
                return account
        raise AccountNotFoundException("account not found")

    def get_accounts(self):
        return len(self.__accounts)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if account.pin == pin:
            self.__accounts.remove(account)
        else:
            raise InvalidPinException("Incorrect PIN")

    def transfer(self, amount, from_account_number, to_account_number, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        from_account.withdraw(amount, pin)
        to_account.deposit(amount)
    # def validate_pin(from_account, pin):
    #     if not from_account.pin == pin:
    #         raise InvalidPinException("Incorrect PIN")
    #
    # def validate_amount_limit(amount, from_account):
    #     if from_account.balance < amount:
    #         raise InsufficientFundsException("Insufficient funds for transfer")
