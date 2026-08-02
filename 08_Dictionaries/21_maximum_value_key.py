students = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 60,
    "Babar": 95
}
print("Dictionary:",students)
keys = list(students.keys())
max_key = keys[0]
max_value = students[max_key]
for key in keys:
    if students[key] > max_value:
        max_value = students[key]
        max_key = key
print("Key with maximum value:", max_key)
print("Maximum value:", max_value)