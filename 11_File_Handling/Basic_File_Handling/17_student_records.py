name = input("Enter your name: ")
roll_no = input("Enter your roll no: ")
marks = input("Enter your marks: ")

with open("students.txt", "a") as f: # append
    f.write(f"Name: {name}\n")
    f.write(f"Roll No: {roll_no}\n")
    f.write(f"Marks: {marks}\n")
print("Records saved successfully")