def palindrome(text):
    result = ""
    for char in text:
        result = char + result
    return result
string = input("Enter a string: ")
reversed_string = palindrome(string)
if reversed_string == string:
    print("Palindrome String")
else:
    print("Not a Palindrome String")