with open("hello.txt","r") as f:
    content = f.readline().strip()
    print("First line is:",content)