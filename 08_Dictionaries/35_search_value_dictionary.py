student = {
    "name" : "Ali",
    "age" : 22,
    "marks" : 75,
    "city" : "New York"
}
print("Dictionary:",student)
value = "New York"
if value in student.values():
    print("Value is in the dictionary")
else:
    print("Value is not in the dictionary")