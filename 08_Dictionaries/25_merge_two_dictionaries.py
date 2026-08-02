student = {
    "name" : "Ali",
    "age" : 25,
    "city" : "Islamabad"
}
marks = {
    "Math" : 60,
    "English" : 70,
    "History" : 80
}
result = student.copy()
result.update(marks)
print("Merged Dictionary:",result)
