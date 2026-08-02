def space(text):
    count = 0
    for char in text:
        if char.isspace():
            count += 1
    return count
string = input("Enter a string: ")
print("Number of spaces: ", space(string))