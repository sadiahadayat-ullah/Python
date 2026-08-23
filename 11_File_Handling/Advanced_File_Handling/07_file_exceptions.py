try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

except OSError:
    print("An operating system error occurred while accessing the file.")