student = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 85,
    "Babar": 95,
    "Ayesha": 70
}
print("Dictionary:",student)
unique = {}
for key, value in student.items():
    if value not in unique.values():
        unique[key] = value

print("Dictionary after removing duplicates:",unique)