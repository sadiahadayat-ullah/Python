balance = 10000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Your Balance is",balance)
elif choice == 2:
    amount = int(input("Enter your amount: "))
    balance = balance + amount
    print("Updated balance is",balance)
elif choice == 3:
    amount = int(input("Enter your amount: "))
    if amount < balance:
        balance -= amount
        print("Updated balance is",balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")