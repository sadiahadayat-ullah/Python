for num in range(1,1001):
    original = num
    length = len(str(num))
    total = 0
    for i in range(length):
        digit = num % 10
        total += digit**length
        num //= 10
    if original == total:
        print(original)