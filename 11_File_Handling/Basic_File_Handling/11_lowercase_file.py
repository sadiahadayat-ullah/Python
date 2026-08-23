with open("hello.txt","r") as f: # read
    text = f.read()
text = text.lower() # Convert text into lowercase

with open("lowercase.txt","w") as f: # write
    f.write(text)

print("Lowercase file created successfully")