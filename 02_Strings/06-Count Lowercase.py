text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isalpha() and ch.islower():
        count += 1
print("Number of lowercase letters:", count)