text = input("Enter a text: ")
vowels = {"a", "e", "i", "o", "u"}
text_letters = set(text.lower())
found_vowels = text_letters & vowels
print("Vowels found:",found_vowels)