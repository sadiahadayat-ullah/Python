entry = input("Enter the message:")

with open("todo_app.txt", "a") as file: # append
    file.write(entry)
    file.write("\n")
print("Message saved successfully")