text1 = input("Enter first string: ").lower()
text2 = input("Enter second string: ").lower()
if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")