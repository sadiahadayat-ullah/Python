num = int(input("Enter a number:"))
original = num
digits = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit**digits
    num = num // 10
if original == total:
    print("Armstrong Number.")
else:
    print("Not a armstrong Number.")