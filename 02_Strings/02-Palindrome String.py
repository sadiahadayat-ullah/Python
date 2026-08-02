text = input("Enter a string: ")
original = text.lower()
reverse = ""
for ch in original:
    reverse = ch + reverse
if original == reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")