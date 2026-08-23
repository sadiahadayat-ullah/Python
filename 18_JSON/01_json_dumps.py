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

json_data = json.dumps(student)
print(json_data)
print(type(json_data))