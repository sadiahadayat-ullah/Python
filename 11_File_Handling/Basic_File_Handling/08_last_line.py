with open("hello.txt", "r") as f:
    content = f.readlines()
    print("Last line is:",content[-1].strip())