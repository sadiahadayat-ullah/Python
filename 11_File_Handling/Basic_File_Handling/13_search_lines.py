with open("diary.txt","r") as f:
    lines = f.readlines()
word = input("Enter a word: ")
for line in lines:
    if word in line:
        print(line.strip())