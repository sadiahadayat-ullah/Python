import json

student = {
    "name": "Ali",
    "age": 18,
    "marks": 92.14,
    "passed": True,
    "address": None,
    "skills": [
        "Python",
        "C++"
    ],
    "course": {
        "name": "Finance",
        "duration": 4
    }
}

json_data = json.dumps(student, indent=4)
print(json_data)
print(type(json_data))

student = json.loads(json_data)
print(student)
print(type(student))