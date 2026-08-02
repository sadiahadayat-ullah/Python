balance = 5000
amount = int(input("Enter withdrawal amount: "))
if amount <= balance:
    if amount > 0:
        print("Withdrawal Successful")
    else:
        print("Withdrawal Failed")
else:
    print("Insufficient Balance")