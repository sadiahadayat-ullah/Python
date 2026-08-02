age = int(input("Enter your age: "))
student = input("Are you a student? yes/no: ")
if age >= 18:
    if student == "yes":
        print("Ticket price: $8")
    else:
        print("Ticket price: $10")
else:
    if student == "yes":
        print("Ticket price: $5")
    else:
        print("Ticket price: $3")