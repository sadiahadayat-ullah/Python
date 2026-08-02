def replace_char(text,old,new):
    result = ""
    for char in text:
        if char == old:
            result += new
        else:
            result += char
    return result
string = input("Enter a string:")
old = "a"
new = "e"
print(replace_char(string,old,new))
