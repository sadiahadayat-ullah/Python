numbers = [10, 20, 30, 10, 20, 10, 40]
print("List of numbers:", numbers)
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("Frequency of elements:", frequency)