units = int(input("Enter number of units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 8
elif units <= 300:
    bill = units * 10
else:
    bill = units * 12
print("Electricity bill is",bill)
