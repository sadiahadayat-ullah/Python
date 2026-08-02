numbers = [10,34,56,78,67,23]
print("Original list:",numbers)
if numbers[0] > numbers[1]
    largest = numbers[0]
    second_largest = numbers[1]
else:
    largest = numbers[1]
    second_largest = numbers[0]
for number in numbers[2:]:
    if number > largest:
       second_largest = largest
       largest = number
    elif number > second_largest and number != largest:
        second_largest = number
print("Largest:",largest)
print("Second Largest:",second_largest)
