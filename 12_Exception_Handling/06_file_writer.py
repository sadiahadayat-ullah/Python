# Program: File writer
# Description: Writes the contents into file

try:
    text = input("Enter text: ")
    with open("dairy.txt","w") as f:
        f.write(text)
    print("File written successfully")

except Exception as e:
    print(e)
