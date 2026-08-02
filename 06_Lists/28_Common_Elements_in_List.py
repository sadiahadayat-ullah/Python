numbers = [10,20,4,10,5,25,5,20]
print("Original list:",numbers)
seen = []
common_elements = []
for number in numbers:
    if number in seen:
        common_elements.append(number)
    else:
        seen.append(number)
print("Common elements:",common_elements)

