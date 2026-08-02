num = int(input("Enter a number: "))
original = num
total = 0
while num > 0:
    digit = num % 10

    factorial = 1
    i = 1
    while i <= digit:
        factorial *= i
        i += 1
    total += factorial
    num //= 10
if original == total:
    print("Strong Number")
else:
    print("Not a Strong Number")