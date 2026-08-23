import json

student = {
    "name": "Ali",
    "age": 18,
    "course": "Finance",
    "skills": [
        "Python",
        "Linux",
        "C++"
    ]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

    print("File created successfully.")
