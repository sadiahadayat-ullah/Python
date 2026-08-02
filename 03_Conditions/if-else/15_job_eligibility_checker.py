age = int(input("Enter your age: "))
degree_status = str(input("Do you have any degree?(yes/no):").lower())
if age >= 18 and degree_status == "yes":
    print("Eligible for the job.")
else:
    print("Not eligible for the job.")