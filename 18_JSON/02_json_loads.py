import json

json_data = '{ "name": "Ali", "age": 18, "course": "Finance"}'

student = json.loads(json_data)
print(student)
print(type(student))
print(student["name"])