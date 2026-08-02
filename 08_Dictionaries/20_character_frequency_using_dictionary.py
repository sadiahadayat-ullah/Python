text = "programming"
print("String:",text)
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Frequency of characters:",frequency)