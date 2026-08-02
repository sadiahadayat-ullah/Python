numbers = [1,2,3,4,5]
print("Original list:",numbers)
numbers = numbers[-1:] + numbers[:-1]
print("Right Rotated list:",numbers)