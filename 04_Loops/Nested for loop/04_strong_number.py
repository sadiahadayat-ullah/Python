num = int(input("Enter a number: "))
original = num
length = len(str(num))
total = 0
for n in range(length):
    digit = num % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i
    total += factorial
    num = num // 10
if original == total:
    print("Strong Number")
else:
    print("Not a Strong Number")