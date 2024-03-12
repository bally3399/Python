import unittest

from oop1.bank import Bank

from oop1.exceptions import InsufficientFundsException


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Gtb Bank")

    def test_register_customer(self):
        self.bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, self.bank.get_accounts())

    def test_find_account(self):
        found_account = self.bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, self.bank.get_accounts())
        self.assertEqual(found_account, self.bank.find_account(101))
        self.assertEqual("Bally Sulaiman", found_account.get_name())

    def test_deposit(self):
        account = self.bank.register_customer("Esther", "Tobiloba", "1234")
        self.bank.deposit(account.get_number(), 1000)
        self.assertEqual(1000, account.get_balance())

    def test_deposit_twice(self):
        account = self.bank.register_customer("Praise", "Oyewole", "1245")
        self.bank.deposit(account.get_number(), 5000)
        self.bank.deposit(account.get_number(), 4000)
        self.assertEqual(9000, account.get_balance())

    def test_withdraw_negative_amount_balance_remains_unchanged(self):
        self.bank = Bank("Gtb Bank")
        account = self.bank.register_customer("Esther", "Tobiloba", "1234")
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(account.get_number(), -1000, "1234")

    def test_withdraw_amount_greater_than_balance_throws_insufficient_funds_exception(self):
        account = self.bank.register_customer("Esther", "Tobiloba", "1234")
        self.bank.deposit(account.get_number(), 500)
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(account.get_number(), 1000, "1234")
        self.assertEqual(500, account.get_balance())

    def test_withdraw(self):
        account = self.bank.register_customer("Esther", "Tobiloba", "1234")
        self.bank.deposit(account.get_number(), 2000)
        self.bank.withdraw(account.get_number(), 1000, "1234")
        self.assertEqual(1000, account.get_balance())

    def test_check_balance(self):
        account = self.bank.register_customer("Bally", "Sulaiman", "1234")
        self.bank.check_balance(account.get_number(), "1234")
        self.assertEqual(0, account.get_balance())

    def test_remove_account(self):
        account = self.bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, self.bank.get_accounts())
        self.bank.remove_account(account.get_number(), "1234")
        self.assertEqual(0, self.bank.get_accounts())

    def test_deposit_1k_transfer_500_my_balance_remains_500(self):
        account1 = self.bank.register_customer("firstName", "LastName", "1234")
        account2 = self.bank.register_customer("first_name", "Last_name", "5678")
        self.assertEqual(2, self.bank.get_accounts())
        self.bank.deposit(account1.get_number(), 1000)

        self.bank.transfer(account1.get_number(), account2.get_number(), 500, "1234")
        self.assertEqual(500, account1.get_balance())
        self.assertEqual(500, account2.get_balance())
