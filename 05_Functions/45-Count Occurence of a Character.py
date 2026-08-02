def count_occurence(text):
    count = 0
    for char in text:
        if char == "a":
            count += 1
    return count
string = input("Enter a string: ")
print("Number of occurence of 'a' in the given string:", count_occurence(string))