numbers = [10,20,30,40,50]
print("Original list:",numbers)
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum:",maximum)