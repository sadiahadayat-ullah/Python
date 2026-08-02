# Using loop
count = 0
with open("hello.txt","r") as f:
    for character in f.read():
        count += 1
    print("Total characters:",count)
# Professional Version
with open("hello.txt","r") as f:
    characters = f.read()
    print("Total characters:",len(characters))