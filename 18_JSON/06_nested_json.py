import json

student = {
    "name": "Ali",
    "age": 18,
    "address": {
        "city": "Lahore",
        "country": "Pakistan"
    },
    "course": {
        "name": "Finance",
        "duration": 4
    },
    "skills": [
        "Python",
        "Linux",
        "C++"
    ]
}

json_data = json.dumps(student, indent=4)
print(json_data)
print(type(json_data))

student = json.loads(json_data)
print(student)
print(type(student))

print(student["name"])
print(student["address"]["city"])
print(student["address"]["country"])
print(student["course"]["name"])
print(student["course"]["duration"])

for skill in student["skills"]:
    print(skill)