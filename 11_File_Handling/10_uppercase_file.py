with open("hello.txt","r") as f: # read
    text = f.read()
text = text.upper() # Convert text into uppercase

with open("uppercase.txt","w") as f: # write
    f.write(text)

print("Uppercase file created successfully")
