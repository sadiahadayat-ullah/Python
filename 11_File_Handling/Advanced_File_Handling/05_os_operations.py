import os

print("Current Directory:", os.getcwd())
print("students.txt file exists:", os.path.exists("students.txt"))
print("Is students.txt a file?", os.path.isfile("students.txt"))
print("Is current loaction a directory?", os.path.isdir("."))
print("Lists and Folders:", os.listdir())