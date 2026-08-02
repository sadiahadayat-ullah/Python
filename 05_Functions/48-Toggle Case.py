def toggle_case(text):
    result = ""
    for char in text:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result
string = input("Enter string: ")
print("Toogle case:", toggle_case(string))