numbers = [10,20,30,5,10,35,20]
print("Original list:",numbers)
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique list:",unique_numbers)