numbers = [10,0,35,45,0,90,0]
print("Original list:",numbers)
new_list = []
zero = []
for number in numbers:
    if number == 0:
        zero.append(number)
    else:
        new_list.append(number)
result = new_list + zero
print("New list:",result)