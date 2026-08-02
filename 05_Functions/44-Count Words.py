def words(text):
    count = 1
    for char in text:
        if char == " ":
            count += 1
    return count
string = input("Enter a string: ")
print("Number of words: ", words(string))