numbers = [10,20,5,10,35,10]
print("Original list:",numbers)
new_list = []
remove = 10
for num in numbers:
    if num != remove:
        new_list.append(num)
print("New list:",new_list)