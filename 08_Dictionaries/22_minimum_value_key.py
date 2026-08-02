students = {
    "Ali": 85,
    "Ahmed": 70,
    "Sara": 60,
    "Babar": 95
}
print("Dictionary:",students)
keys = list(students.keys())
min_key = keys[0]
min_value = students[min_key]
for key in keys:
    if students[key] < min_value:
        min_value = students[key]
        min_key = key
print("Key with minimum value is:",min_key)
print("Minimum value:",min_value)