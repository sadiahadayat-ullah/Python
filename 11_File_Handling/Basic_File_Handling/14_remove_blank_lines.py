cleaned_list = []

with open("hello.txt","r") as f: # read
    lines = f.readlines() # read all lines as list
for line in lines:
    if line.strip():
        cleaned_list.append(line)

with open("cleaned.txt","w") as f: # write
    f.writelines(cleaned_list)
    
print("Successfully cleaned")