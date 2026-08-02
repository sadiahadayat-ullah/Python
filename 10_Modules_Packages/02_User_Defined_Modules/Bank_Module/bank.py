"""
This module  contains bank-related information.
"""

def check_balance(balance):
    """returns the current balance"""
    return f"Current balance: ${balance}"
def deposit(balance, amount):
    """adds money to the balance"""
    return f"Deposited ${balance + amount}"
def withdraw(balance, amount):
    """subtracts money from the balance"""
    return f"Withdrawn ${balance - amount}"
def account_holder(name):
    """returns the account holder name"""
    return f"Account Holder {name}"

bank_name = "ABC bank"
country = "Pakistan"

if __name__ == "__main__":
    print("Bank module is running directly")
    print(check_balance(1000))