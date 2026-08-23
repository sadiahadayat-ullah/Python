import json

with open("student.json", "r") as file:
    student = json.load(file)

skill = input("Enter skill to search: ")

if skill in student["skills"]:
    print("Skill found.")
else:
    print("Skill not found.")

course = input("Enter course to search: ")

if course == student["course"]:
    print("Course found.")
else:
    print("Course not found.")