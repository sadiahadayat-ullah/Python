def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    print("\n===== Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "5":
        print("Program is excited")
        break
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    if choice == "1":
        print("Addition:", add(number1,number2))
    elif choice == "2":
        print("Subtraction:", sub(number1,number2))
    elif choice == "3":
        print("Multiplication:", mul(number1,number2))
    elif choice == "4":
        print("Division:", div(number1,number2))
    else:
        print("Invalid choice")
