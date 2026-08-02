# Program: File Reader
# Description: Reads the file content using exception handling

try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print("File not found")
    print(e)

finally:
    print("Program finished")