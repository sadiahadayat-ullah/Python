# Program: Object Identity
# Description: Demonstrates that each object has a unique identity (memory address) using the id() function.


class Student:
    pass

student1 = Student()
student2 = Student()

print(id(student1))
print(id(student2))