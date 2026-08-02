def compare(text1,text2):
    if text1 != text2:
        return False
    for i in range(len(text1)):
        if len(text1[i]) != len(text2[i]):
            return False
    return True
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if compare(string1,string2):
    print("Strings are equal")
else:
    print("Strings are not equal")