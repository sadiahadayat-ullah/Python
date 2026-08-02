import os
path = "01_current_directory.py"
if os.path.exists(path):
    print("File exists")
else:
    print("File does not exist")