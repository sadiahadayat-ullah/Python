import datetime
today_date = datetime.date.today()
new_date = datetime.date(2027, 1, 1)
difference = new_date - today_date
print(f"The difference is {difference.days} days")