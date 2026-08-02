with open("hello.txt",'r') as source: # read
    content = source.read()
with open("hello.txt",'w') as destination: # write
    destination.write(content)
print("File copied successfully")
