with open("students.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    print(line1.strip())
    print(line2.strip())
    print(line3.strip())