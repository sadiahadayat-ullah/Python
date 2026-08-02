text = input("Enter a string:")
count = 0
for ch in text:
    if ch.isalpha() and ch.isupper():
        count += 1
print("Number of uppercase letters:", count)
