numbers = (1,2,3,4,5,6)
print(numbers)
even = ()
odd = ()
for number in numbers:
    if number % 2 == 0:
       even = even + (number,)
    else:
        odd = odd + (number,)
print("Even numbers:",even)
print("Odd numbers:",odd)