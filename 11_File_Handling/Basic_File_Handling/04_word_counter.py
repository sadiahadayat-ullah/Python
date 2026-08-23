# Using loop
count = 0
with open("hello.txt","r") as f:
    for words in f.read().split():
        count = count + 1
    print("Total words:",count)
# Professional Version
with open("hello.txt","r") as f:
    words = f.read().split()
    print("Total words:",len(words))