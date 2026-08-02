numbers = [1,2,3,2,1]
print("Original list:",numbers)
original = numbers.copy()
reversed_numbers = []
for number in reversed(numbers):
    reversed_numbers.append(number)
if original == reversed_numbers:
    print("Palindrome List")
else:
    print("Not Palindrome")