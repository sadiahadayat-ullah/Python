import json

with open("student.json", "r") as file:
    student = json.load(file)

    print(student)
    print(type(student))

    print(student["name"])
    print(student["skills"][1])