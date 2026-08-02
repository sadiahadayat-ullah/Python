num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum = 0
for i in range(digits):
    digit = num % 10
    sum += digit**digits
    num = num // 10
if original == sum:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")