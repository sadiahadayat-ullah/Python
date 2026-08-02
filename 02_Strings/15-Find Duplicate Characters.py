string = input("Enter a string: ")
seen = ""
duplicates = ""
for ch in string:
    if ch not in seen:
        seen += ch
    elif ch not in duplicates:
        duplicates += ch
print("Duplicates: ", duplicates)