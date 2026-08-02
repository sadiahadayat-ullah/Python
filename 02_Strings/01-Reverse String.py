text = input("Enter a string: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Original string: " + text)
print("Reversed string: " + reverse)