print("Hotel Booking")
print("1. Standard Room")
print("2. Deluxe Room")
choice = int(input("Enter your choice: "))
if choice == 1:
    breakfast = input("Do you want breakfast? (yes/no): ")
    if breakfast == "yes":
        print("Standard Room with Breakfast - $60")
    else:
        print("Standard Room without Breakfast - $50")
elif choice == 2:
    breakfast = input("Do you want breakfast? (yes/no): ")
    if breakfast == "yes":
        print("Deluxe Room with Breakfast - $95")
    else:
        print("Deluxe Room without Breakfast - $80")
else:
    print("Invalid Choice")