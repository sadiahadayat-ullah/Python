years = int(input("Enter number of years: "))
if years >= 10:
    print("Bonus: $1000")
elif years >= 5:
    print("Bonus: $500")
elif years >= 3:
    print("Bonus: $300")
elif years >= 2:
    print("Bonus: $200")
elif years >= 1:
    print("Bonus: $100")
else:
    print("No Bonus")