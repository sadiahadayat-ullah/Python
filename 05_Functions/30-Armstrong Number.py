def armstrong(n):
    total = 0
    length = len(str(n))
    for i in range(length):
        digit = n % 10
        total += digit**length
        n = n // 10
    return total
number = int(input("Enter a number: "))
armstrong_number = armstrong(number)
if armstrong_number == number:
    print("Armstrong Number")
else:
    print("not an Armstrong Number")
