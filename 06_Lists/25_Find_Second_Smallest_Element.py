numbers = [10,34,56,78,67,23]
print("Original list:",numbers)
smallest = numbers[0]
second_smallest = numbers[1]
if second_smallest < smallest:
    smallest, second_smallest = second_smallest, smallest
for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
       second_smallest = number
print("Smallest:",smallest)
print("Second smallest:",second_smallest)