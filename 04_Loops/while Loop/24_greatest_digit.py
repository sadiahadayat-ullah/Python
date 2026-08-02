num = int(input("Enter a number:"))
greatest = 0
while num > 0:
    digit = num % 10

    if digit > greatest:
        greatest = digit
    num = num // 10
    print("The greatest digit is", greatest)