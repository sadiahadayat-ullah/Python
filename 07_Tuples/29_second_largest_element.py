numbers = (10,20,45,78,88,33)
print("Tuple:",numbers)
if numbers[0] > numbers[1]:
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
print("Second largest:",second_largest)
