num = 1
while num <= 1000:
    original = num
    temp = num
    digits = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit**digits
        temp //= 10
    if original == total:
        print(original)
    num += 1