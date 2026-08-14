# Program: Bank Account Balance
# Description: Demonstrates how to access a private balance using a public method.

class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Bank Balance:",self.__balance)

bank_account = BankAccount()
bank_account.show_balance()