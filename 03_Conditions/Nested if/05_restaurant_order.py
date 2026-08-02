print("1. Pizza")
print("2. Burger")
choice = int(input("Enter your choice: "))
if choice == 1:
    size = int(input("Enter your size: "))
    if size == "small":
        print("Small pizza")
    else:
        print("Large pizza")
elif choice == 2:
    print("Burger")
else:
    print("Invalid choice")
