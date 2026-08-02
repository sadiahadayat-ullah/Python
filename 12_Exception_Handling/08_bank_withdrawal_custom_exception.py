# Program: Bank Withdrawal
# Description: Withdraws money using a custom exception.

class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    print("Withdrawal amount:",amount)
    balance -= amount
    print("Remaining balance:",balance)

except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("Please enter valid amount")
    
finally:
    print("Program finished")