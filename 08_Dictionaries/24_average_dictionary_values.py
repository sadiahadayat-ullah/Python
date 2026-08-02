students = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 60,
    "Babar": 95
}
print("Dictionary:",students)
total = 0
for value in students.values():
    total += value
average = total / len(students)
print("Total:",total)
print("Average:",average)