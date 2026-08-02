python_course = {"Ali", "Ahmed", "Sara", "Zeeshan"}
ai_course = {"Ahmed", "Sara", "Usman", "Ayesha"}
# Students enrolled in both courses
common_students = python_course & ai_course
# Students enrolled only in python course
only_python_course = python_course - ai_course
# Students enrolled only in ai course
only_ai_course = ai_course - python_course
# All students in both courses
all_students = python_course | ai_course
print("Common students:",common_students)
print("Students only in python course:",only_python_course)
print("Students only in ai course:",only_ai_course)
print("All students:",all_students)