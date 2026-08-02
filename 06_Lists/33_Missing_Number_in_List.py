numbers = [1,2,3,5,6]
print("Original list:",numbers)
for i in range(1,7):
    if i not in numbers:
        numbers.append(i)
        print("Missing number:",i)
numbers.sort()
print("New list:",numbers)