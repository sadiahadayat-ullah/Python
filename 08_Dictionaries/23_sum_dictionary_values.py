students = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 60,
    "Babar": 95
}
print("Dictionary:",students)
total = 0
for key, value in students.items():
    total = total + value
print("Total:",total)