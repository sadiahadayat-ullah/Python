age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")
if age >= 18:
    if citizen == "yes":
        print("You are a citizen")
    else:
        print("You are not a citizen")
else:
    print("You are under 18")