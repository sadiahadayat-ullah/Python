numbers = (10,20,45,78,88,33)
print("Tuple:",numbers)
smallest = numbers[0]
second_smallest = numbers[1]
if smallest > second_smallest:
    smallest, second_smallest = second_smallest, smallest
for number in numbers[2:]:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif smallest < number < second_smallest:
       second_smallest = number
print("Smallest:",smallest)
print("Second smallest:",second_smallest)