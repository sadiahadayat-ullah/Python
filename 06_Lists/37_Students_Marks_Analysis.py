marks = [75,90,68,82,95]
print("Student marks:",marks)
print("Maximum marks:",max(marks))
print("Minimum marks:",min(marks))
print("Average marks:",sum(marks)/len(marks))
passed = 0
failed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1
print("Passed:",passed)
print("Failed:",failed)