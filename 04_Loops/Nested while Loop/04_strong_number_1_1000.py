num = 1
while num <= 1000:
    original = num
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        i = 1
        factorial = 1
        while i <= digit:
            factorial *= i
            i += 1
        total += factorial
        temp //= 10
    if original == total:
        print(original)
    num += 1