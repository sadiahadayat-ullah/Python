from student_management import student
from student_management import teacher
from student_management import attendance
from student_management import  result
from student_management import classroom

print(student.student_info("Ali",17))

print(teacher.teacher_subject("Computer"))
print(teacher.teacher_info("Ahmed"))

print(attendance.student_status("Ali",True))

percentage = result.calculate_percentage(55,100)
print("Percentage:",percentage)
print("Status:",result.status_pass(percentage))

print(classroom.classroom_info(12,"A"))
