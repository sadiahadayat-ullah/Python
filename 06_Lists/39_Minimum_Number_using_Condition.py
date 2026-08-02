numbers = [10,20,30,35,5]
print("Original list:", numbers)
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print("Minimum number:", minimum)