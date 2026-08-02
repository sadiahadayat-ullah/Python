with open("diary.txt","r") as f:
    text = f.read()
word = input("Enter a word: ")
words = text.split()
total = text.count(word)
print(word,"appears",total,"times")