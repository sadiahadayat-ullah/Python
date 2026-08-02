num = int(input("Enter a number: "))
reverse = 0
length = len(str(num))
for i in range(length):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("The reverse number is:", reverse)