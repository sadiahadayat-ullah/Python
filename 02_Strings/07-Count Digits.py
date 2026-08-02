text = input("Enter a string: ")
count = 0
digits = ""
for ch in text:
    if ch.isdigit():
        digits += ch
        count += 1
print("Number of digits:", count)
print("Digits:", digits)