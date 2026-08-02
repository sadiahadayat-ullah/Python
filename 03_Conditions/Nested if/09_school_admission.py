age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 7:
    if marks >= 60:
        print("You are eligible for admission")
    else:
        print("You are not eligible for admission.")
else:
    if marks >= 60:
        print("You are under 7, so you can't join school.")
    else:
        print("You are under 7, and your marks are also insufficient.")