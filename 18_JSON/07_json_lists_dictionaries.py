import json

student = {
    "name": "Ali",
    "age": 18,
    "skills": [
        "Python",
        "Linux",
        "C++"
    ],
    "courses": [
        "Finance",
        "Programming",
        "Database"
    ]
}

json_data = json.dumps(student, indent=4)
print(json_data)
print(type(json_data))

student = json.loads(json_data)
print(student)
print(type(student))

for skill in student["skills"]:
    print(skill)

for course in student["courses"]:
    print(course)

student["skills"].append("Java")
print(student["skills"])
print(student["skills"][1])