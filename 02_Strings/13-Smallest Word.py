sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    smallest = words[0]
    for word in words:
        if len(word) < len(smallest):
            smallest = word
print("Smallest Word: ", smallest)