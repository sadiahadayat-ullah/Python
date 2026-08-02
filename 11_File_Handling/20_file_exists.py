import os

file_name = input("Enter your file name: ")
os.path.exists(file_name)
if os.path.exists(file_name):
    print("File exists")
else:
    print("File not exists")