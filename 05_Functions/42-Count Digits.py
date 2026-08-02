def digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count
string = input("Enter a string: ")
print("Number of digits: ", digits(string))