def perfect(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total
number = int(input("Enter a number: "))
perfect_number = perfect(number)
if perfect_number == number:
    print("Perfect Number")
else:
    print("Not a perfect number")