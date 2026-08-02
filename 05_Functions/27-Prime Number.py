def prime(num):
    Prime = True
    for i in range(2,num):
        if num % i == 0:
            Prime = False
            break
    return Prime
if prime(7):
    print("Prime Number")
else:
    print("Not a Prime Number")

