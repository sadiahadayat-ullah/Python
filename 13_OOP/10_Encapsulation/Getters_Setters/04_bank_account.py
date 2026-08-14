# Program: Bank Account Using Getter and Setter
# Description: Demonstrates how to access and modify a private account balance using getter and setter methods with validation.

class BankAccount:

    def __init__(self):
        self.__account_holder = "Ali"
        self.__balance = 10000

    def get_account_holder(self):
        return self.__account_holder
    def get_balance(self):
        return self.__balance

    def set_account_holder(self,account_holder):
        self.__account_holder = account_holder
    def set_balance(self,balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

bank_account = BankAccount()
print("Account Holder Name:", bank_account.get_account_holder())
print("Account Balance:", bank_account.get_balance())

bank_account.set_account_holder("Ahmed")
print("Updated Account Holder Name:", bank_account.get_account_holder())

bank_account.set_balance(20000)
print("Updated Balance:", bank_account.get_balance())

bank_account.set_balance(-10000)
print("Updated Balance:", bank_account.get_balance())