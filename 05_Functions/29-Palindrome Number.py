def num(n):
    original = n
    temp = n
    reverse = 0
    length = len(str(n))
    for i in range(length):
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    return reverse
number = int(input("Enter a number: "))
reversed_number = num(number)
if number == reversed_number:
    print("Palindrome Number")
else:
    print("Not a Palindrome")
