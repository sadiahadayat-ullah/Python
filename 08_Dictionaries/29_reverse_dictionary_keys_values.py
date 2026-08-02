student = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 85,
    "Babar": 95,
    "Ayesha": 70
}
print("Original Dictionary:",student)
reverse = {}
for key, value in student.items():
    reverse[value] = key
print("Reversed Dictionary:",reverse)


