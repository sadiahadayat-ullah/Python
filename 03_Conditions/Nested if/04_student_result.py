marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
if marks >= 50:
    if attendance >= 75:
        print("Pass")
    else:
        print("Attendance is low")
else:
    print("Fail")
