numbers = (1,2,3,4,5)
print("Tuple:",numbers)
even = ()
odd = ()
for number in numbers:
    if number % 2 == 0:
        even += (number,)
    else:
        odd += (number,)
print("Even numbers:",even)
print("Odd numbers:",odd)
# Count even and odd
print("Length of even numbers:",len(even))
print("Length of odd numbers:",len(odd))