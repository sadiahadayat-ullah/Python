import json

with open("student.json", "r") as file:
    student = json.load(file)

    student["age"] = 20
    student["course"] = "Database"
    student["skills"].append("Java")

    print(student)

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

    print("Student file updated.")

