import datetime
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
birthday = datetime.date(year, month, day)
weekday = birthday.strftime("%A")
print(f"The weekday is {weekday}")