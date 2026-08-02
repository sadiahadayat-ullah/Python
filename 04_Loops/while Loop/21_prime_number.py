num = int(input("Enter a number:"))
i = 2
prime = True
while i < num:
    if num % i == 0:
        prime = False
        break
    i += 1
if prime and num >1:
    print("Prime Number")
else:
    print("Not a Prime Number")