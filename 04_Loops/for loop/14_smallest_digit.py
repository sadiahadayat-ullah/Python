num = int(input("Enter a number: "))
smallest = 9
length = len(str(num))
for i in range(length):
    digit = num % 10

    if digit < smallest:
        smallest = digit
    num = num // 10
print("The smallest digit is", smallest)