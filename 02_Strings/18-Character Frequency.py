string = input("Enter a string: ")
new_string = ""
for ch in string:
    if ch not in new_string:
        print(ch,":",string.count(ch))
        new_string += ch