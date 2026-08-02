for n in range(1,101):
    original = n
    reverse = 0
    length = len(str(n))
    for i in range(length):
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        print(original)