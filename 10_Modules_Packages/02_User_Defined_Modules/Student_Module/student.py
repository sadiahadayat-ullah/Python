"""
This module contains student-related information.
"""

def student_info(name,age):
    """returns the student's name and age"""
    return f"Name: {name}, Age: {age}"
def student_grade(grade):
    """returns the student's grade"""
    return f"Grade: {grade}"
def student_school(school):
    """returns the student's school"""
    return f"School: {school}"
def student_city(city):
    """returns the student's city"""
    return f"City: {city}"

school = "DPS"
country = "Pakistan"

if __name__ == "__main__":
    print("Student module is running directly")
    print(student_info("Ali",12))