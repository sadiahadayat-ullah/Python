string = input("Enter a string: ")
new_text = ""
for ch in string:
    if ch not in new_text:
        new_text += ch
print("After removing duplicates: ", new_text)