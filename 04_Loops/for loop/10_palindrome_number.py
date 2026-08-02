num = int(input("Enter a number: "))
original = num
reverse = 0
length = len(str(num))
for i in range(length):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a palindrome")