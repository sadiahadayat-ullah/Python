def count(num):
    total = 0
    length = len(str(num))
    for i in range(length):
        total += 1
    return total
number = int(input("Enter a number: "))
print("Number of digits: ", count(number))
