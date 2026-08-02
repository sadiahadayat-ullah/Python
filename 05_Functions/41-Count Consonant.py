def consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of consonants: ", consonants(string))
