# Using Loop
count = 0
with open("hello.txt","r") as f:
    for line in f.readlines():
        count = count + 1
    print("Total lines:",count)
# Professional Version
with open("hello.txt","r") as f:
    lines = f.readlines()
    print("Total lines:",len(lines))