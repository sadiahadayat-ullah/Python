def reverse(num):
    rev = 0
    length = len(str(num))
    for i in range(length):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
num = 123
print("Original number:",num)
print("Reversed number:",reverse(num))