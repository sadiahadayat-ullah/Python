for num in range(1,1001):
    original = num
    length = len(str(num))
    total = 0
    for n in range(length):
        digit = num % 10

        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        total += factorial
        num //= 10
    if original == total:
        print(original)