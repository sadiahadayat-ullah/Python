from datetime import datetime

entry = input("Enter the line: ")

with open("diary.txt","a") as f: # append
    f.write(str(datetime.now())+"\n")
    f.write(entry+"\n")

print("Diary entry saved successfully.")