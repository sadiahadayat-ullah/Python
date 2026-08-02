numbers = [10,20,56,10,25,20,5]
print("Original list:",numbers)
seen = []
duplicates = []
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)
print("Duplicates:",duplicates)