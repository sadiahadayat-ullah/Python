numbers = [10,13,54,77,47,5,56]
print("Original list:", numbers)
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Count Even:", len(even))
print("Count Odd:", len(odd))