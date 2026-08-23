import json

try:
    with open("student.json", "r") as file:
        student = json.load(file)

    print(student)

except FileNotFoundError:
    print("JSON file not found.")

except json.JSONDecodeError:
    print("Invalid JSON data.")

except OSError:
    print("An operating system error occurred while accessing the file.")