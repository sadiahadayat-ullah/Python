def reverse(text):
    result = ""
    for char in text:
        result = char + result
    return result
string = input("Enter a string: ")
print(reverse(string))