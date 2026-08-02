num = 1
while num <= 100:
    original = num
    temp = num
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    if original == reverse:
        print(original)
    num += 1