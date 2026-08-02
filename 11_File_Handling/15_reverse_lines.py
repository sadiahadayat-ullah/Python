reversed_list = []

with open("hello.txt","r") as f: # read
    lines = f.readlines()
for line in lines:
    reversed_list.append(line.strip()[::-1] + "\n")

with open("reverse.txt","w") as f: # write
    f.writelines(reversed_list)
print("Lines reversed successfully")