numbers = (10,20,30,40,50)
print("Tuple:",numbers)
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Sum:",total)
print("Average:",average)