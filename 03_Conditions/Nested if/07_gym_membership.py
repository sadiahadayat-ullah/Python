age = int(input("Enter your age: "))
medical_certificate = input("Are you healthy? (yes/no): ")
if age >= 18:
    if medical_certificate == "yes":
        print("You are eligible to join gym.")
    else:
        print("You are not eligible to join gym.")
else:
    if medical_certificate == "yes":
        print("you are under 18, so you can't join gym.")
    else:
        print("You are under 18, and don't have a medical certificate.")