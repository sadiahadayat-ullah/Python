import os
filename = "01_current_directory.py"
size = os.path.getsize(filename)
file_path = os.path.abspath(filename)
print("Size:",size)
print("File path:",file_path)
