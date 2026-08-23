with open("students.txt", "r") as file:
    print("Initial Position:", file.tell())

    content = file.read(5)
    print("Characters:", content)

    print("Position:", file.tell())

    file.seek(0)

    print("Position after seek:", file.tell())

    content2 = file.read(5)
    print("Next Characters:", content2)